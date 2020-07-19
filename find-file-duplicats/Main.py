import os
import ConfigLoader

class Logger():
    def __init__(self):
        # add date in log's filename
        self.logFile = "/tmp/logfile.log"


class DuplicatsFinder():
    def __init__(self, rootDirPath):
        self.rootDirPath = "/home/grzesiek/Documents"

    def find(self):
        filePaths = {}
        for root, _, files in os.walk(self.rootDirPath):
            for filename in files:
                if filename in filePaths:
                    foundSimilarFilePaths = filePaths[filename]
                    foundSimilarFilePaths.append("{}/{}".format(root,filename))
                else:
                    filePaths[filename] = ["{}/{}".format(root, filename)]

        for file in filePaths.values():
            if (len(file) > 1):
                print(filePaths)


if __name__ == "__main__":
    configLoader = ConfigLoader()
    d = DuplicatsFinder(configLoader.rootFilePath())
    d.find()
