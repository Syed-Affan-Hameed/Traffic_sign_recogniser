import os
import sys
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import pickle
import pyspark

from sklearn.model_selection import train_test_split
from tensorflow.keras.models import load_model
from sklearn.metrics import accuracy_score

import numpy as np
import tensorflow.keras as tfk
from traffic import load_data

with open(r'CNN-Traffic-Signs-Recognetion-TensorFlow-And_Keras-main\CNN-Traffic-Signs-Recognetion-TensorFlow-And_Keras-main\test.pkl', 'rb') as f:
	x_test, y_test = pickle.load(f)
y_test =np.argmax(y_test, axis=1)

model = load_model(r'CNN-Traffic-Signs-Recognetion-TensorFlow-And_Keras-main\CNN-Traffic-Signs-Recognetion-TensorFlow-And_Keras-main\model2.h5')
prediction = np.argmax(model.predict(x_test), axis=1)
print(prediction[0] + 1)
accuracy = float(accuracy_score(y_test, prediction.round()))
print('The accuracy of the model on test set is {:.2f}'.format(accuracy * 100), "%")

# dictionary to label all traffic signs class.
classes = {1: 'Speed limit (20km/h)',
           2: 'Speed limit (30km/h)',
           3: 'Speed limit (50km/h)',
           4: 'Speed limit (60km/h)',
           5: 'Speed limit (70km/h)',
           6: 'Speed limit (80km/h)',
           7: 'End of speed limit (80km/h)',
           8: 'Speed limit (100km/h)',
           9: 'Speed limit (120km/h)',
           10: 'No passing',
           11: 'No passing veh over 3.5 tons',
           12: 'Right-of-way at intersection',
           13: 'Priority road',
           14: 'Yield',
           15: 'Stop',
           16: 'No vehicles',
           17: 'Veh > 3.5 tons prohibited',
           18: 'No entry',
           19: 'General caution',
           20: 'Dangerous curve left',
           21: 'Dangerous curve right',
           22: 'Double curve',
           23: 'Bumpy road',
           24: 'Slippery road',
           25: 'Road narrows on the right',
           26: 'Road work',
           27: 'Traffic signals',
           28: 'Pedestrians',
           29: 'Children crossing',
           30: 'Bicycles crossing',
           31: 'Beware of ice/snow',
           32: 'Wild animals crossing',
           33: 'End speed + passing limits',
           34: 'Turn right ahead',
           35: 'Turn left ahead',
           36: 'Ahead only',
           37: 'Go straight or right',
           38: 'Go straight or left',
           39: 'Keep right',
           40: 'Keep left',
           41: 'Roundabout mandatory',
           42: 'End of no passing',
           43: 'End no passing veh > 3.5 tons'}

# initialise GUI
top = tk.Tk()
top.geometry('1500x900')
top.title('Traffic sign Predictor')
top.configure(background='#CDCDCD')

label = Label(top, background='#CDCDCD', font=('arial', 18, 'bold'))
sign_image = Label(top)


def classify(file_path):
	global label_packed
	image = Image.open(file_path)
	image = image.resize((30, 30))
	image = np.expand_dims(image, axis=0)
	image = np.array(image)
	print(image.shape)
	pred = model.predict_classes([image])[0]
	sign = classes[pred + 1]
	print(sign)
	label.configure(foreground='#364196', text=sign)


def show_classify_button(file_path):
	classify_b = Button(top, text="Classify Image", command=lambda: classify(file_path), padx=10, pady=5)
	classify_b.configure(background='#364196', foreground='white', font=('arial', 10, 'bold'))
	classify_b.place(relx=0.79, rely=0.46)


def upload_image():
	try:
		file_path =filedialog.askopenfilename()
		uploaded = Image.open(file_path)
		uploaded.thumbnail(((top.winfo_width() / 2.25), (top.winfo_height() / 2.25)))
		im = ImageTk.PhotoImage(uploaded)

		sign_image.configure(image=im)
		sign_image.image = im
		label.configure(text='')
		show_classify_button(file_path)
	except:
		pass


upload = Button(top, text="Upload a traffic sign image", command=upload_image, padx=10, pady=5)
upload.configure(background='#364196', foreground='white', font=('arial', 10, 'bold'))

upload.pack(side=BOTTOM, pady=70)
sign_image.pack(side=BOTTOM, expand=True)
label.pack(side=BOTTOM, expand=True)
heading = Label(top, text="Predict Your Traffic Sign", pady=40, font=('Times New Roman', 25, 'bold'))
heading.configure(background='#CDCDCD', foreground='#364196')
heading.pack()
top.mainloop()