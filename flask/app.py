import os
from flask import Flask, render_template, request
from PIL import Image
from resizeimage import resizeimage


app = Flask(__name__)


APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'uploads/')

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist('image-to-test'):
        filename = file.filename
        destination = '/'.join([target, filename])
        file.save(destination)
        print(destination)
        img = Image.open(destination)
        print(img)
        img = resizeimage.resize_height(img, 100)
        img = resizeimage.resize_width(img, 100)
        print(img.format)
        img.save(destination, 'JPEG')
        print(img)

    return render_template('success.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
