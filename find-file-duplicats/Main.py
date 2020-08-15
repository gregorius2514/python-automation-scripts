import os
import ConfigLoader
import hashlib

class Logger():
    def __init__(self):
        # add date in log's filename
        self.logFile = "/tmp/logfile.log"


class DuplicatsFinder():
    def __init__(self, rootDirPath):
        self.rootDirPath = "/tmp"

    def find(self):
        duplicatedFilePaths = {}
        for root, _, files in os.walk(self.rootDirPath):
            for filename in files:
                fileHash = self.hashFile(filename)
                if fileHash in duplicatedFilePaths:
                    foundSimilarDuplicatedFilePaths = duplicatedFilePaths[fileHash]
                    foundSimilarDuplicatedFilePaths.append("{}/{}".format(root,filename))
                else:
                    duplicatedFilePaths[fileHash] = ["{}/{}".format(root, filename)]

        for file in duplicatedFilePaths.values():
            if (len(file) > 1):
                print(duplicatedFilePaths)

    def hashFile(self, filepath):
        READ_FILE_CHUNK = 2048
        fileHash = hashlib.sha3_256()

        with open(filepath,"rb") as file:
            for fileBytes in iter(lambda: file.read(READ_FILE_CHUNK), b""):
                fileHash.update(fileBytes)

        return fileHash.hexdigest()

if __name__ == "__main__":
    configLoader = ConfigLoader()
    d = DuplicatsFinder(configLoader.rootFilePath())
    d.find()
