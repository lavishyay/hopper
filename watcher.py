from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import mover
import os

path = '{0}'.format(os.path.abspath(''))

class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None
        elif event.event_type == "moved":
            event_path = '{0}'.format("\\".join(event.src_path.split("\\")[:-1]))
            if event_path == path:
                i = mover.File(event.dest_path)
                if i.exten == "crdownload" or i.exten == "part":
                    pass
                else:
                    if i.dest != __file__ and i.name != mover.configname:
                        i.category = mover.category
                        i.categorize()
                        i.move()
                        print(f"{event.dest_path} moved to -> {i.path}")
                    else:
                        pass 

class Watcher():
    def __init__(self):
        self.observer = Observer()
        self.path = '{0}'.format(os.path.abspath(''))
        
    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.path, recursive = True)
        
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")
 
        self.observer.join()

if __name__ == "__main__":
    watch = Watcher()
    watch.run()
    