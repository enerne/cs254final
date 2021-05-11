# TensorFlow and tf.keras
import tensorflow as tf
import matplotlib.pyplot as plt
import get_data
import numpy as np


x_train: np.array
(x_train, x_test), (y_train, y_test) = get_data.get_all_splits()
