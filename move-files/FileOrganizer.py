from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path

OUTPUT_PATH = "/tmp/output"
outputPath = Path(OUTPUT_PATH)

class FilesChanges(FileSystemEventHandler):

    def on_created(self, event):
        p = event.src_path
        print("create: {}".format(p))
        path = Path(p)
        if path.is_file():
            extension = path.suffix
            if extension != '':
                dir = outputPath.joinpath(extension.replace('.',''))
                dir.mkdir()
                path.rename(dir.joinpath(path.name))

if __name__ == "__main__":
    observer = Observer()
    observer.schedule(FilesChanges(), "/tmp/test", recursive=True)

    observer.start()
    observer.join()
