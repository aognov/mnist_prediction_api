
"""
simple python flask application
"""

##########################################################################
## Imports
##########################################################################

import os

from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
from flask.json import jsonify
import pandas as pd
import numpy as np
import tensorflow as tf

##########################################################################
## Application Setup
##########################################################################

app = Flask(__name__)

##########################################################################
## Routes
##########################################################################


@app.route('/classify/', methods=['GET','POST'])
def get_classify():
    if(request.method == 'POST'):
        pixels = request.get_json()['pixels']
        test_label =  request.get_json()['label']
        pixels_array = np.array([pixels])
        
        test_image = pd.DataFrame(pixels_array, columns=np.arange(784))
        test_image = np.float32(test_image/255.0)
        test_image = test_image.reshape(-1, 28, 28)
        class_names = ['T-shirt/top',' Trouser', 'Pullover', ' Dress', ' Coat', ' Sandal', ' Shirt', ' Sneaker', ' Bag', 'Ankle boot']

        model = tf.keras.models.load_model('mnist_model.h5')
        predictions = model.predict( test_image)
        predicted_label = np.argmax(predictions)
        
        return jsonify({"true label": class_names[test_label], "label predicted": class_names[predicted_label]})
    else :
        return render_template("home.html")

##########################################################################
## Main
##########################################################################

if __name__ == '__main__':
    app.run()
