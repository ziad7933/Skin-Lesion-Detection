import os
import cv2 #NOT ESSENTIAL FOR UPLOAD HANDLING
from flask import Flask, render_template, session,  redirect, url_for
from flask_wtf import FlaskForm
from flask_uploads import configure_uploads, IMAGES, UploadSet
from wtforms import FileField

# NO NEED TO CHANGE
app = Flask(__name__)

app.config['SECRET_KEY'] = "HelloHello"
app.config['UPLOADED_IMAGES_DEST'] = 'uploads/images'


images = UploadSet('images', IMAGES)
configure_uploads(app, images)

class MyForm(FlaskForm):
    image = FileField('image')
  

# This function handles all the picture submissions  
# This will take a picture and create a folder called
# uploads/images and store all the uploaded images there
# this function can be accessed on 
# http://127.0.0.1:5000/ 

# NO NEED TO CHANGE
@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        filename = images.save(form.image.data)
        session['my_var'] = filename
        # return f'Congrats! you uploaded a picture. Filename: {filename}'
        return redirect(url_for('imageReader'))

    return render_template('index.html', form=form)


# ML model

import warnings
warnings.filterwarnings('ignore',category=FutureWarning)
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
tf.get_logger().warning('test')
tf.get_logger().setLevel('ERROR')
tf.get_logger().warning('test')

import sys,getopt
import tensorflow
import numpy as np
from tensorflow.keras.models import Model
from tensorflow.keras.metrics import categorical_accuracy, top_k_categorical_accuracy
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing import image
from tensorflow.keras.layers import Dense, Dropout


def top_3_accuracy(y_true, y_pred):
    return top_k_categorical_accuracy(y_true, y_pred, k=3)

def top_2_accuracy(y_true, y_pred):
    return top_k_categorical_accuracy(y_true, y_pred, k=2)


mobile = tensorflow.keras.applications.mobilenet.MobileNet()
type(mobile.layers)
len(mobile.layers)

# Architechture
x = mobile.layers[-6].output
x = Dropout(0.25)(x)
predictions = Dense(7, activation='softmax')(x)
model = Model(inputs=mobile.input, outputs=predictions)
model = Model(inputs=mobile.input, outputs=predictions)


model.load_weights('model.h5')

class_labels = ['actinic keratosis/Bowens disease (intraepithelial carcinoma) (AKIEC)',
'Basal Cell Carcinoma (BCC)',
'Benign Keratosis (solar lentigo/seborrheic keratosis/lichen planus-like keratosis) (BKL)',
'Dermatofibroma (DF)',
'Melanoma (MEL)',
'Melanocytic Nevus (NV)',
'Vascular Lesion (VASC)']


def loadImages(path):
  img = image.load_img(path,target_size=(224, 224))
  img_data = image.img_to_array(img)
  img_data = np.expand_dims(img_data, axis=0)
  img_data = tensorflow.keras.applications.mobilenet.preprocess_input(img_data)
  features = np.array(model.predict(img_data))
  y_classes = features.argmax(axis=-1)
#   print (features)
  return y_classes



# this is the result displayed on the frontend
@app.route('/imageReader')
def imageReader():

    fname = session.get('my_var', None)
    upldPth = 'uploads\\images\\'
    fullFilePath =  upldPth + fname 
    x = loadImages(fullFilePath)
    
    return render_template('imageStats.html', label=class_labels[x[0]])
