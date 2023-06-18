import time
from watchdog.observers import Observer
from src.tools.file_event_handler import FileEventHandler


event_handler = FileEventHandler()
observer = Observer()
observer.schedule(event_handler, "input_shipment/", recursive=False)

observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
