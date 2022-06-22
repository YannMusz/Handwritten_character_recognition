from prediction import predict_letter

from flask import Flask, jsonify, render_template, request
import cv2
from imageio import imread
import io
import base64
from PIL import Image
import time
import numpy as np

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/", methods = ["POST", "GET"])
def welcome():
    "Testing"
    return render_template("index.html")

@app.route("/prediction", methods = ["POST", "GET"])
def predict():
    params = request.get_json()

    #print function for flask
    app.logger.info(params["letter"])

    ## in js remember to have the object with key "letter" and transform it to base 64
    picture = params["letter"]

    while params is None: 
        time.sleep(2)
    else: 
        prediction = predict_letter(picture)

        # img = imread(io.BytesIO(base64.b64decode(picture)))

        #FROM YANN
        # nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
        # img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        # print(img.shape)
        app.logger.info("it works")
        # prediction = predict_letter(img)
    
    # when http request name the response from the server response 
    return jsonify(response = prediction)

    # return jsonify(response = params["letter"])
    # return jsonify(response = imread(io.BytesIO(base64.b64decode(params["letter"]))))
   


if __name__ == '__main__':
    app.run(debug=True)
