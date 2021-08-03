import time
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import requests


def post_file2server(src):
    server_addrs = "http://127.0.0.1:5000/upload"
    data = {'file': open(src, 'rb')}

    getdata = requests.post(server_addrs, files=data)

    print(getdata.text)

class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track+'/'+filename
            post_file2server(src)


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


