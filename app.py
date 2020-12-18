# Import libraries

# Flask 
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

# Keras
from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import model_from_json
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array

import numpy as np
import os
import sys
import glob
import re
import h5py

import PIL
from PIL import Image

# Buat flask instance
app = Flask(__name__)


# Load model

MODEL_ARCHITECTURE =  'model/model_plant_disease_1.json'   
MODEL_WEIGHTS = 'model/model_plant_disease_weight.h5'

json_file = open(MODEL_ARCHITECTURE)
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)

model.load_weights(MODEL_WEIGHTS)
print('@@ Model loaded. Check http://127.0.0.1:5000/')



def model_predict(img_path, model):
  test_image = load_img(img_path, target_size = (224, 224)) # load image 
  print("@@ Got Image for prediction")
  
  test_image = img_to_array(test_image)/255 # normalisasi dan ubah ke array
  test_image = np.expand_dims(test_image, axis = 0) 
  
  
  result = model.predict(test_image) # prediksi 
  
  pred = np.argmax(result, axis=1) # ambil indexnya



# 3/4/6/10/14/17/19/22/23/24/27/37
           
  if   pred == 0: #Apple___Apple_scab
      return 'Tanamanmu Sakit', 'disease_plant_apple_scab.html' # sudah diisi
  elif pred == 1: #Apple___Black_rot
      return 'Tanamanmu Sakit', 'disease_plant_apple_black_rot.html'   
  elif pred == 2: #Apple___Cedar_apple_rust
      return 'Tanamanmu Sakit', 'disease_plant_apple_cedar_apple_rust.html'  
  elif pred == 5: #Cherry_(including_sour)___Powdery_mildew
      return 'Tanamanmu Sakit', 'disease_plant_cherry_powdery_mildew.html' 
  elif pred == 7: #Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot
      return 'Tanamanmu Sakit', 'disease_plant_corn_gray_leaf_spot.html' 
  elif pred == 8: #Corn_(maize)___Common_rust_
      return 'Tanamanmu Sakit', 'disease_plant_corn_common_rust.html' 
  elif pred == 9: #Corn_(maize)___Northern_Leaf_Blight
      return 'Tanamanmu Sakit', 'disease_plant_corn_northern_leaf_blight.html' 
  
  # Jeda   
  elif pred == 11: #Grape___Black_rot
      return 'Tanamanmu Sakit', 'disease_plant_grape_black_rot.html' 
  elif pred == 12: #Grape___Esca_(Black_Measles)
      return 'Tanamanmu Sakit', 'disease_plant_grape_esca.html' 
  elif pred == 13: #Grape___Leaf_blight_(Isariopsis_Leaf_Spot)
      return 'Tanamanmu Sakit', 'disease_plant_grape_leaf_blight.html' 
  elif pred == 15: #Orange___Haunglongbing_(Citrus_greening)
      return 'Tanamanmu Sakit', 'disease_plant_orange_haunglongbing.html'
  elif pred == 16: #Peach___Bacterial_spot
      return 'Tanamanmu Sakit', 'disease_plant_peach_bacterial_spot.html' 
  elif pred == 18: #Pepper,_bell___Bacterial_spot
      return 'Tanamanmu Sakit', 'disease_plant_pepper_bacterial_spot.html' 
  elif pred == 20: #Potato___Early_blight
      return 'Tanamanmu Sakit', 'disease_plant_potato_early_blight.html' 
  
  # Jeda   
  elif pred == 21: #Potato___Late_blight
      return 'Tanamanmu Sakit', 'disease_plant_potato_late_blight.html' 
  elif pred == 25: #Squash___Powdery_mildew 
      return 'Tanamanmu Sakit', 'disease_plant_squash_powdery_mildew.html'    
  elif pred == 26: #26 Strawberry___Leaf_scorch 
      return 'Tanamanmu Sakit', 'disease_plant_strawberry_leaf_scorchy.html' # sudah diisi
  elif pred == 28: #28 Tomato___Bacterial_spot 
      return 'Tanamanmu Sakit', 'disease_plant_tomato_bacterial_spot.html' # sudah diisi
  elif pred == 29: #Tomato___Early_blight
      return 'Tanamanmu Sakit', 'disease_plant_tomato_early_blight.html' 
  elif pred == 30: #Tomato___Late_blight
      return 'Tanamanmu Sakit', 'disease_plant_tomato_late_blight.html' 
  
  # Jeda
  elif pred == 31: #Tomato___Leaf_Mold
      return 'Tanamanmu Sakit', 'disease_plant_tomato_leaf_mold.html' 
  elif pred == 32: #Tomato___Septoria_leaf_spot
      return 'Tanamanmu Sakit', 'disease_plant_tomato_septoria_leaf_spot.html' 
  elif pred == 33: #Tomato___Spider_mites Two-spotted_spider_mite
      return 'Tanamanmu Sakit', 'disease_plant_tomato_spider_mites.html' 
  elif pred == 34: #Tomato___Target_Spot
      return 'Tanamanmu Sakit', 'disease_plant_tomato_target_spot.html' 
  elif pred == 35: #Tomato___Tomato_Yellow_Leaf_Curl_Virus
      return 'Tanamanmu Sakit', 'disease_plant_tomato_yellow_leaf.html'  
  elif pred == 36: #Tomato___Tomato_mosaic_virus
      return 'Tanamanmu Sakit', 'disease_plant_tomato_mosaic_virus.html' 
  else:
      return "Tanamanmu Sehat", 'healthy_plant.html'
    
    


# render index.html page
@app.route("/", methods=['GET', 'POST'])
def home():
        return render_template('index.html')
    
# ambil input gambar lalu prediksi dan menampilkan halaman .html 
@app.route("/predict", methods = ['GET','POST'])
def predict():
     if request.method == 'POST':
        file = request.files['image'] # fet input
        filename = file.filename        
        print("@@ Input posted = ", filename)
        
        file_path = os.path.join('static/user uploaded', filename)
        file.save(file_path)

        print("@@ Predicting class......")
        pred, output_page = model_predict(file_path, model)
              
        return render_template(output_page, pred_output = pred, user_image = file_path)
    
# for local system & cloud
if __name__ == "__main__":
    app.run(threaded=False,) 
    
    