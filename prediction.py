
import tensorflow as tf
import numpy as np
import base64

model_dir = 'mnist-model/'
saved_model = tf.saved_model.locad(model_dir)
predictor = saved_model.signatures['default']


#user does not pass integer, random integer is selected automatically
def predict():
    # Select a random example
    selected_element        = np.random.randint(0, 9999)

    features                = test_features[selected_element].reshape((28,28))
    label                   = test_labels[selected_element]

    plt.imshow(features, cmap="Greys")

    actual_label            = str(label)
    single_predicated_label = str(model.predict(features.reshape((1,28,28,1)))[0].argmax())
    
    return {'prediction': single_predicted_label}

print(predict())
#test prediction function ===========================================
#prediction = predict(single_test_text)  
#print('returned prediction: ' + prediction)
