from prediction import predict_letter

from flask import Flask, jsonify, render_template, request
import time

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

    ## in js remember to have the object with key "letter" and transform it to base 64
    picture = params["letter"]

    while params is None: 
        time.sleep(2)
    else: 
        prediction = predict_letter(picture)
    
    # when http request name the response from the server response 
    return jsonify(response = prediction)
   


if __name__ == '__main__':
    app.run(debug=True)
