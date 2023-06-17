import time
from watchdog.observers import Observer
from services.file_event_handler import FileEventHandler


event_handler = FileEventHandler()
observer = Observer()
observer.schedule(event_handler, "", recursive=False)

observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()