# First try to setup a for loop that echos back a message
import os
import subprocess
from flask import Flask, request
from config import ROOT_DIR

app = Flask(__name__)


from flask import request
from werkzeug.utils import secure_filename


def upload_to_cloud(src):
    subprocess.run(['gsutil', 'cp', src, 'gs://xuanhua-backup-bucket/'])




@app.route('/upload', methods=['GET', 'POST'])
def upload_file():

    if request.method == 'POST':
        f = request.files['file']

        src = 'server_storage/' + secure_filename(f.filename)


        if not os.path.exists(ROOT_DIR+"/server_storage"):
            os.makedirs(ROOT_DIR+"/server_storage")

        f.save(src)
        upload_to_cloud(src)
        os.remove(src)

        return "post received"
    else:
        return "Hello!"


if __name__ == '__main__':
    app.run(host='0.0.0.0')



