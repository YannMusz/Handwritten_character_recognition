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
