# Interactive MNIST Demo
### Or: 0 to AI in 3 notebooks

This set of notebooks takes you through a gentle introduction to one of the most basic AI problems, the MNIST dataset

MNIST is a dataset of 60,000 handwritten digits, which is used as input to train an AI. The AI learns the relationship between the pixel values, the arrangement, and the digit. The AI then is able to label arbitrary handwritten digits.

This will require:
  * A Linux system (tested on Fedora)
  * Python 3
  * Python 3 virtualenv module
  * The ability to untar .tar.gz files
  * Docker (with the ability for users to spawn containers, or you can copy the relevant line out of the notebook)
  * Access to the internet for pip installs and docker pulls

To get started, simply run the `start.sh` script. Interrupt it (crtl +c) to stop

Once the notebook server is running (it should automatically open the browser), follow the notebooks in numbered order:
  * 01-MNIST-Data-Exploration: Covers some of the basics about data exploration and gives an intro to the MNIST dataset
  * 02-MNIST-TensorFlow: Covers creating the model, what layers are important, why to use certain ones, and training, testing, and saving the model
  * 03-Serving-TensorFlow-Locally: Covers the operations side of serving the model using docker, as well as using a provided webapp to interact with the model


When fully done, the cleanup.sh script will ensure docker is properly cleaned up, and the virtualenv is removed
