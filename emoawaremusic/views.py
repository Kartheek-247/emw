from django.shortcuts import render
import cv2
import pandas as pd
import os
import glob as gb
import random
import subprocess
from tensorflow import keras
import tensorflow
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Create your views here.
def home_page(request):
    if request.method=="POST":
            model_path = "model1.h5"
            print("_"*40,os.getcwd()+"\model1.h5")
            loaded_model = keras.models.load_model(model_path)
            camera_port=0    #camera 0 is laptop camera
            ramp_frames=30    #30 frames pause before taking a picture to adjust
            camera=cv2.VideoCapture(camera_port)  #establishesthe camera

            #captures a single image from the camera and return it in PIL format
            def get_image():
                retval,im=camera.read()
                return im

            for i in range(ramp_frames):
                temp=get_image()
            print("Capturing image...")

            #takes the picture
            camera_capture=get_image()
            file='test_image.png'
            cv2.imwrite(file, camera_capture)

            #releases the camera
            del camera
            print("picture taken.")

            image = cv2.imread("test_image.png") 

            image_fromarray = Image.fromarray(image, 'RGB')

            resize_image = image_fromarray.resize((128, 128))
            expand_input = np.expand_dims(resize_image,axis=0)
            input_data = np.array(expand_input)
            input_data = input_data/255

            pred = loaded_model.predict(input_data)
            result = pred.argmax()

            #mp = 'C:/Program Files (x86)/Windows Media Player/wmplayer.exe'
            if result==0:
                '''randomfile = random.choice(os.listdir("C:\\Users\\kartheek\Desktop\\Angry\\"))
                print("It seems you are 'ANGRY'")
                file=("C:\\Users\\kartheek\Desktop\\Angry\\"+randomfile)
                subprocess.call([mp,file])
                cv2.destroyAllWindows()'''
                res="anger"
            if result==1:
                '''randomfile = random.choice(os.listdir("C:\\Users\\kartheek\Desktop\\Disgust\\") )   
                print("It seems you are 'Disgust'")
                file=("C:\\Users\\kartheek\Desktop\\Disgust\\"+randomfile)
                subprocess.call([mp,file])
                cv2.destroyAllWindows()'''
                res="disgust"
            if result==2:
                '''randomfile = random.choice(os.listdir("C:\\Users\\kartheek\Desktop\\Fear\\"))
                print("It seems you are 'Fear'")
                file=("C:\\Users\\kartheek\Desktop\\Fear\\"+randomfile)
                subprocess.call([mp,file])
                cv2.destroyAllWindows()'''
                res="fear"
            if result==3:
                '''randomfile = random.choice(os.listdir("C:\\Users\\kartheek\Desktop\\Happy\\"))
                print("It seems you are 'Happy'")
                file=("C:\\Users\\kartheek\Desktop\\Happy\\"+randomfile)
                subprocess.call([mp,file])
                cv2.destroyAllWindows()'''
                res="happy"
            if result==4:
                '''randomfile = random.choice(os.listdir("C:\\Users\\kartheek\Desktop\\Sad\\"))                           
                print("It seems you are 'Sad'")
                file=("C:\\Users\\kartheek\Desktop\\Sad\\"+randomfile)
                subprocess.call([mp,file])
                cv2.destroyAllWindows()'''
                res="sad"
            if result==5:
                '''randomfile = random.choice(os.listdir("C:\\Users\\kartheek\Desktop\\Surprise\\"))
                print("It seems you are in 'Surprise'")
                file=("C:\\Users\\kartheek\Desktop\\Surprise\\"+randomfile)
                subprocess.call([mp,file])
                cv2.destroyAllWindows()'''
                res='surprise'

            return render(request,"index.html",context={"resexp":res,"listed":1})
    return render(request,"index.html",context={"resexp":"happy","listed":0})