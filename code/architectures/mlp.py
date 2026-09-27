"""
Author: Marina Vicens Miquel

This file contians the AI architecture
"""

# Importing libraries 
from tensorflow.keras.layers import Input
from tensorflow.keras.layers import Dense
from keras.models import Model
from tensorflow import keras


# Creating a class where the AI architecture is defined
class mlp_model():
    
    # Initializing the arguments passed
    def __init__(self, input_shape):
        self.input_shape = input_shape  
        
    # Defining the AI architecture and returning the model
    def model(self):
        
        data_input = Input(self.input_shape)
        x = Dense(2, activation='sigmoid', kernel_regularizer='l2')(data_input)
        output = Dense(1)(x)
        
        model = Model(inputs=[data_input], outputs=output)
        
        return model