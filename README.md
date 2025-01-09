# ResNet_GAWS


This is the Git repository for a ResNet based CNN model for aberration estimation interms of Zernike polynomials in a Grating Array based Wavefront Sensor

## Setting up

The program was developed in Python 3.12.7 with Tensorflow '2.18.0' (CPU). 

I would suggest you use [Anaconda](https://www.anaconda.com/download/success) / Miniconda and set up a virtual environment as:

- `conda create -n "myenv" ` # replace "myenv" with your desired name.

After setting up the virtual environment, activate it using `conda activate "myenv" ` using anaconda prompt and install tensorflow in it as:

- `pip install tensorflow-cpu`

Alternatively, you can use [Google Colab](https://colab.research.google.com/) to process your code.

## Usage

- data_generation.ipynb : this notebook is used to generate training as well as testing data for the CNN model
- RESNET_model.ipynb : this is the main notebook which predicts the aberration strengths from focal spots array

A step-by-step procedure for using each notebook is incorporated into the notebooks.

Thank you,

Pranjal Choudhury
