# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 13:00:51 2022

@author: Leonard 
"""

import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

from keras import models 
from keras import layers 
from keras import optimizers
from keras import regularizers
from keras.callbacks import EarlyStopping
from keras.callbacks import ModelCheckpoint
from keras.utils.vis_utils import model_to_dot
from keras.utils import plot_model
from keras.models import load_model

from IPython.display import SVG

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder

from sklearn.model_selection import  train_test_split

training = pd.read_csv("Diabetes.csv")
training= pd.get_dummies(training, columns=['Gender'], prefix='',drop_first=False)
data = training

x = data.iloc[:,data.columns!='CLASS'].values.astype('float32')
y = data.loc[:,"CLASS"].values

#Encoding and scaling relevant data
#0=N,2=Y,1=P
label = LabelEncoder()
scale = StandardScaler()
y=label.fit_transform(y).astype('int')
#scale everything besides encoded values _M & _F
x[:,:12] = scale.fit_transform(x[:,:12])

#### spliting the train test data into 2 
x_train, x_val_and_test,y_train, y_val_and_test = train_test_split(x, y, test_size=0.2)
#splitting it yet again into RANDOM train and test subsets 
x_val,x_test,y_val,y_test = train_test_split(x_val_and_test, y_val_and_test, test_size=0.5)

print("Dimensions of each of the train and test datasets:")
print('x_train=>',x_train.shape,"\tx_val=>",x_val.shape,"\tx_test=>",x_test.shape)
print('y_train=>',y_train.shape, "\ty_val=>",y_val.shape,"\t\ty_test=>",y_test.shape)

model = models.Sequential()
model.add(layers.Dense(16,activation='relu',input_shape=(x_train.shape[1],)))
model.add(layers.Dense(7,activation='relu'))
model.add(layers.Dense(3,activation='relu'))
model.add(layers.Dense(1))
#optimiser=optimizers.RMSprop(lr=0.1)#0.00015
model.compile(loss='mse', optimizer='rmsprop', metrics=['mae'])

#Setting callback functions to stop training early and save the best model so far 
callbacks = [EarlyStopping(monitor='val_loss', patience=2), ModelCheckpoint(filepath='diabetes_model.h5', monitor='val_loss',save_best_only=True)]
#Train network
history = model.fit(x_train,y_train,validation_data=(x_val, y_val),batch_size=3 ,epochs=60, callbacks=callbacks)

#model evalutation
model.evaluate(x_test,y_test)

#saving model to a file
#plot_model(model,show_shapes=True, to_file="model.jpg")