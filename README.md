# Skin Lesion Detection
Skin Lesion is one of the most dangerous and unnoticed diseases people face. These diseases do not look as menacing as it sounds since most people just ignore it thinking it is a mole. Additionally, detecting the disease is also a hassle as the diagnosis takes long. With the prowess of Machine Learning, this problem can be solved quickly. The above files have two Deep Learning models that can detect skin lesions. The system will take in an image and give you an output on the type of skin disease it is. The model can only detect 7 skin lesions because of the limitations of the dataset.

## Dataset
The dataset used for this project is the [Skin Cancer MNIST:HAM10000](https://www.kaggle.com/kmader/skin-cancer-mnist-ham10000) dataset from Kaggle. It contains 10,000 dermatoscopic images of skin lesions for training Machine Learning models. The dataset contains images from 7 different skin lesions which are given below along with their respective abbreviations used in the code:
- Actinic keratoses and intraepithelial carcinoma / Bowen's disease (akiec)
- Basal cell carcinoma (bcc)
- Benign keratosis-like lesions (solar lentigines / seborrheic keratoses and lichen-planus like keratoses, bkl)
- Dermatofibroma (df)
- Melanoma (mel)
- Melanocytic nevi (nv)
- Vascular lesions (angiomas, angiokeratomas, pyogenic granulomas and hemorrhage, vasc)

## About the Model and their Results
There are two models in the folder, one that uses a pretrained ResNet18 and the other uses MobileNet where the last 5 layers are customized with dropouts and added dense layers with Softmax activation for predictions. The results after running each of the models is given below:
##### ResNet18
- Validation Accuracy = 91.73%
- Validation Loss = 29.13%

##### MobileNet
- Validation Loss = 33.22%
- Categorical Accuracy = 89.45%
- Top 2 Accuracy = 96.38%
- Top 3 Accuracy = 99.04%

## Dataset Setup
- Download the dataset from [here](https://www.kaggle.com/kmader/skin-cancer-mnist-ham10000).
- Clone the repository to your PC.
- Extract the dataset into the folder containing the ```.ipynb``` files.
- Just run any one of the ```.ipynb``` files and specify the directory of the dataset according to the examples used in the code.
- If you are using Google Colab, upload the dataset in Google Drive, load up the drive in Colab by running the ```drive.mount()``` cell and copy the path in place.
- For both of the models, the datasets do not need to be changed as the code will use the dataset as it is. 
- The MobileNet model will create another directory, separate the dataset into training and test set and then create 7 more directories for each of the diseases using the ```metadata.csv``` included with the dataset. It will copy all the images to their respective directories.

## WebApp Deployment
The project is deployed using a Flask. The saved model is called and a prediction is shown in the console which is then deployed in Flask to create a webpage. To run the app, you have to extract the ```FlaskApp.rar``` file and open a virtual environment.

## Setting up the Virtual Environment
Open command prompt and navigate to the where you want to set up the application the type in the following:
```
virtualenv {foldername}
```
Replace the foldername with your own and remove the curly braces. Once run, you should see a folder with the name given in the directory. Now place the files from the FlaskApp folder into the virtual environment you just created. You can place your saved model inside the folder, make sure the saved model is of ```.h5``` file format.

Use command prompt to navigate inside the folder and then type in the following to activate the virtual environment.
```
Scripts\activate
```
## How to run
With the virtual environment up and running, install the dependencies from the requirements file. Type in the following:
```
pip install -r requirements.txt
```
And then type the following as there is an error with Werkzeug's version which crashes the local server when executed.
```
pip install -U Werkzeug==0.16.0
```
Once the dependencies are installed, type in:
```
flask run
```
This should take a minute to load and you will see an address in the console which you can copy and paste in your browser and access the webpage. 

## Developer Notes
This project is not meant to replace the existing medical methodologies and diagnosis. The sole purpose of this project is to use Machine Learning Algorithms to solve problems in the medical field.
