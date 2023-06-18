import time
from watchdog.observers import Observer
from src.processor.file_event_processor import FileEventProcessor


if __name__ == "__main__":
    event_handler = FileEventProcessor()
    observer = Observer()
    observer.schedule(event_handler, "input_shipment/", recursive=False)

    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
