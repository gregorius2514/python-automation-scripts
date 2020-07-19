import sys, os, time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from shutil import copyfile

class FilesChanges(FileSystemEventHandler):
    def on_modified(self, event):
        p = event.src_path

        if os.path.isfile(p):
            absPath = os.path.abspath(p)
            fileName = os.path.basename(p)
            extension = os.path.splitext(fileName)[1].replace('.', '')
            destinationPath = '/tmp/{}'.format(extension)

            if not os.path.exists(destinationPath):
                os.mkdir(destinationPath)

            copyfile(absPath, '/tmp/{}/{}'.format(extension,fileName))

if __name__ == "__main__":
    observer = Observer()
    observer.schedule(FilesChanges(), ".", recursive=True)

    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()