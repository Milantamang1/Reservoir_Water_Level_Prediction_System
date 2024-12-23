from keras.saving import register_keras_serializable
from tensorflow.keras.layers import LSTM
import numpy as np
import pickle
import tensorflow as tf
import keras

# Define your custom LSTM class
@tf.keras.utils.register_keras_serializable()
class CustomLSTM(tf.keras.layers.Layer):
    def __init__(self, units=64, **kwargs):
        super(CustomLSTM, self).__init__(**kwargs)
        self.units = units

    def build(self, input_shape):
        self.kernel = self.add_weight(
            shape=(input_shape[2], self.units),
            initializer='glorot_uniform',
            name='kernel'
        )
        self.recurrent_kernel = self.add_weight(
            shape=(self.units, self.units),
            initializer='orthogonal',
            name='recurrent_kernel'
        )
        self.bias = self.add_weight(
            shape=(self.units,),
            initializer='zeros',
            name='bias'
        )
        super(CustomLSTM, self).build(input_shape)

    def call(self, inputs):
        h_t = tf.zeros_like(inputs[:, 0, :])  # Initial hidden state
        c_t = tf.zeros_like(inputs[:, 0, :])  # Initial cell state

        for t in range(inputs.shape[1]):
            x_t = inputs[:, t, :]
            h_t, c_t = self.step(x_t, h_t, c_t)
        return h_t

    def step(self, x_t, h_t, c_t):
        z_t = tf.matmul(x_t, self.kernel)
        z_t += self.bias
        h_t_new = tf.nn.tanh(z_t)
        c_t_new = h_t_new
        return h_t_new, c_t_new
