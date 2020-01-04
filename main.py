import time
import shutil
import os
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

if __name__ == "__main__":
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitivity = True
    my_event_handler = PatternMatchingEventHandler(
        patterns, ignore_patterns, ignore_directories, case_sensitivity)

    def on_created(event):
        new_file = event.src_path
        file_extension = new_file.split('.').pop()
        print (new_file)
        print (file_extension)
        print("{} has been created!".format(event.src_path))
        if not os.path.exists('./' + file_extension):
            os.mkdir(file_extension)
        shutil.move(new_file, './' + file_extension)

    # def on_modified(event):
    #     print("{} has been modified".format(event.src_path))

    # def on_moved(event):
    #     print("{} moved to {}".format(
    #         event.src_path, event.dest_path))

    my_event_handler.on_created = on_created
    # my_event_handler.on_modified = on_modified
    # my_event_handler.on_moved = on_moved

    path = "."
    go_recursively = False
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=go_recursively)

    my_observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()
