import numpy as np
import cv2
import os
from PIL import Image
#from tensorflow import keras
from tensorflow.keras.models import model_from_json
from colorama import Fore, Back
#import tensorflow as tf

RESULT_LIST = ["Positive, Bacterial", "Negative", "Positive, Viral"]

def create_model(model_file):
    with open(model_file, "r") as json_file:
        loaded_model_json = json_file.read()
        loaded_model_json = model_from_json(loaded_model_json)
    return loaded_model_json



def run_predictions(path_to_img):
    model = create_model("model/model.json")
    model.load_weights("model/weights.h5")
    #print(model.summary())
    img = cv2.imread(path_to_img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #width, height = img.shape[:2]
    img = cv2.resize(img , (200, 200))
    res = np.argmax(model.predict(img[np.newaxis, :, :]))
    if (res == 0):
        print(Fore.MAGENTA + Back.BLACK + "Positive, Bacterial")
    elif (res == 1):
        print(Fore.GREEN + Back.BLACK + "Negative")
    else:
        print(Fore.CYAN + Back.BLACK + "Positive, Viral")


input_img = input("Enter image name: ")

path_to_img = os.path.join("images", input_img)
run_predictions(path_to_img)

