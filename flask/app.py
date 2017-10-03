import os
from flask import Flask, render_template, request
from PIL import Image
import numpy as np
from resizeimage import resizeimage
import h5py
# import neuralnet
#
#
# # hyper-parameters
# layers_dims = [30000, 20, 5, 1]  # all images should be 100 x 100 px so input layer is 30000 in length.
# learning_rate = 0.0075
# training_set = {}
# print_cost = True
# num_iterations = 3000


# neuralnet.L_layer_model(X, Y, layers_dims, learning_rate, num_iterations, print_cost)

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
        img = Image.open(destination)
        img = resizeimage.resize_height(img, 100)
        img = resizeimage.resize_width(img, 100)
        img.save(destination, 'JPEG')
        img = np.array(Image.open(destination))
        img = img.flatten()
        img = img.reshape((img.shape[0], 1))
        print(img.shape)

        # This is where the AI will run and then delete the photo after
        # results are calculated. Should return a json object with data on
        # classification.

    return render_template('success.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
