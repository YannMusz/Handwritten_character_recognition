
# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
import cv2

# Load the trained model
trained_model = load_model("character_recog_model.h5")

# Recompile the model 
trained_model.compile(optimizer="adam", loss="binary_crossentropy", metrics = ["accuracy"])

# Create words dictionary

words = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X', 24:'Y',25:'Z'}

# Function to predict letter characters using the trained model
def predict_letter(img_path):
    # Read the image using cv2
    image = cv2.imread(img_path)

    # make copy of original image, copy will be used to change colors
    image_copy = image.copy()

    # convert image to RGB using cvtColor
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Resize image to 400 x 400 size
    image = cv2.resize(image, (400,400))

    # Add blur to image and greyscale (need to greyscale as cv.threshold needs greyscale images)
    image_copy = cv2.GaussianBlur(image_copy, (7,7), 0)
    grey_image = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)


    # Separate object from background pixels using thresholding
    # https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
    _, img_thresh = cv2.threshold(grey_image, 100, 255, cv2.THRESH_BINARY_INV)

    # Resize and reshape image to fit trained_model requirements
    final_image = cv2.resize(img_thresh, (28,28))
    final_image = np.reshape(final_image, (1, 28, 28, 1))

    # Make prediction using the trained_model
    prediction = words[np.argmax(trained_model.predict(final_image))]

    print(f"The prediction is: {prediction}" )
    return prediction

#Test that file is working 
#predict_letter("C.png")