import tensorflow as tf
import keras
import numpy as np
import base64

#load mnist-model.h5
model = keras.models.load_model('mnist-model/mnist-model.h5')

#user does not pass integer, random integer is selected automatically
def predict():
    # Select a random example
    selected_element        = np.random.randint(0, 9999)

    features                = test_features[selected_element].reshape((28,28))
    label                   = test_labels[selected_element]

    plt.imshow(features, cmap="Greys")

    actual_label            = str(label)
    single_predicted_label  = str(model.predict(features.reshape((1,28,28,1)))[0].argmax())
    
    print("Features:")
    print("Actual label: " + str(label))
    print("Predicted label: " + str(model.predict(features.reshape((1,28,28,1)))[0].argmax()))
    
    return {'prediction': single_predicted_label}

#test function
predict()

