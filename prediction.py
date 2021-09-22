import tensorflow as tf
import keras
import numpy as np
import base64
import os
import pandas as pd
import matplotlib.pyplot as plt

#load model mnist-model.h5
model = keras.models.load_model('mnist-model/mnist-model.h5')

######################################################################################################
#Predict function does not take in any parameters.  A random integer is selected automatically.
#The function will return:  the actual label and the predicted label
######################################################################################################

train_df: pd.DataFrame     = pd.read_csv('Resources/mnist_train.csv', header=None)
test_df: pd.DataFrame      = pd.read_csv('Resources/mnist_test.csv', header=None)
    
train_features: np.ndarray = train_df.loc[:, 1:].values
train_features             = train_features.reshape((train_features.shape[0], 28, 28, 1))
train_features             = train_features / 255.0

train_labels: np.ndarray   = train_df[0].values

test_features: np.ndarray  = test_df.loc[:, 1:].values
test_features              = test_features.reshape((test_features.shape[0], 28, 28, 1))
test_features              = test_features / 255.0
test_labels: np.ndarray    = test_df[0].values

#user does not pass integer, random integer is selected automatically
def predict():
    # Select a random example
    selected_element        = np.random.randint(0, 9999)
    
    features                = test_features[selected_element].reshape((28,28))
    label                   = test_labels[selected_element]
    
    #print image of selected element
    selected_image = plt.imshow(features, cmap="Greys")  
    
    #use model to predict the actual numeric equivalent of mnist image
    single_predicted_label  = str(model.predict(features.reshape((1,28,28,1)))[0].argmax())

    return {'prediction': selected_image}

predict()

