
import time
import sys
import argparse
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import subprocess

class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track+'/'+filename

            subprocess.run(['gsutil','cp',src,'gs://xuanhua-backup-bucket/'])

# parsing input arguements here


folder_to_track = sys.argv[1]


observer = Observer()
event_handler = Handler()
observer.schedule(event_handler,
                  folder_to_track,
                  recursive=True)

observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()



