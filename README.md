# Handwritten Character Recognition

## Why Image Recognition?

We decided to create a Handwritten Character Recognition application as it involves challenging oursevles to apply our knowledge of deep learning, JavaScript, HTML, and CSS. Additionally, Image recognition technology is increasingly relevant in todays environment.

### It's relevant

Image recognition technology has many applications, including labeling content of images with meta-tags, guiding autonomous robots or self-driving cars, and performing image content search.

### It involves deep learning

To create an image recognition application, a Convolutional Neural Network (CNN) model, supported by tensorflow and keras, is typically used to recognize characters.

## Description of Source Data

The dataset was obtained from [kaggle](https://www.kaggle.com/datasets/sachinpatel21/az-handwritten-alphabets-in-csv-format?resource=download)

It contains 26 folders (A-Z) containing handwritten images in size 2828 pixels, each alphabet in the image is centre fitted to 2020 pixel box.

Each image is stored as Gray-level.

Kernel CSVToImages contains script to convert .CSV file to actual images in .png format in structured folder.

## Questions to Answer

Can we create a model to accurately recognize handwritten characters?

## The machine Learning Model

### Preliminary Data Preprocessing

- In the csv file, images are present in 784 columns of pixel data.
- We can reshape the image data to 28 x 28 pixels using numpy to display in the form of an image.
- Once an image is reshaped, we can display it in a window using cv2.imshow()
- We can also use matplotlib to display the image in jupyter notebook.

### Splitting the Data

We split the data into X and y. X contains a character image and y contains a label of that image.

### Convolutional Neural Networks Model

#### Background Considerations

At its core, an image is a 2D array of pixels. Therefore, any image should be able to be classified based on its features (pixels).

#### Why did we select a CNN model?

Convolutional Neural Network models are specifically designed for processing image data (pixels). They are widely used for image processing and recognition.

#### What is a CNN?

CNN is a combination of Convolutional Layers and Neural Network. It consists of:

1. An Input Layer
2. Convolutional Layers
3. Pooling Layers
4. Dense Layers

### how does our CNN model work?

- Step 1: Feed the input layer of the neural network an array with pixels of the handwritten character
- Step 2: Use convolutional layers to extract image features and return them in the form of a matrix
  A ReLu activation function is applicad after every convolution to transform the output values between the range 0 and 1.
- Step 3: Use a Pooling Layer to reduce the size of the matrix
  This helps the model to deal with overfitting by providing an abstract representation and also reduces the computational cost.
- Step 4: Flatten the data to convert a 2D matrix into a vector
  After the convolution and pooling layers, the data is flattened into a feedforward neural network which is also called a Multi-Layer Perceptron.
- Step 5: Feed the flattened data into the Dense Layer to classify the image based on the output from the convolutional layers
  A dense layer is a neural network layer that receives input from all neurons of its previous layer. Our model uses the relu activation function for 2 dense layers and softmax activation function for the output layer.

### Limitations and Benefits of the Model

Limitations

- Hard to classify images with different positions
- Hard to classify images with different backgrounds or under different lighting conditions
- CNN is slow
- A large dataset is needed to train the neural network

Benefits

- Automatically detects the important features without any human supervision
  Fast to implement and relatively easy to understand
