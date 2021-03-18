from PIL import Image
import constants as c
import os
# sklearn utilities
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
import numpy as np
import matplotlib.pyplot as plt


def get_test_train(images, label):
    if __name__ == "__main__" or True:
        print(label)

    y = np.array([c.value_of[label]] * len(images))
    return (np.array(i) for i in train_test_split(images, y, test_size=0.25, random_state=0))


def get_data_from(image):
    data = image.getdata()
    arr = np.array(data)
    arr = arr.flatten()
    return arr

def get_all_splits():
    dir = "output/data/train"
    # 8196, 6147 train 2049 test
    master_x_train = master_y_train = np.empty(shape=(6147, 12288,))
    master_x_test = master_y_test = np.empty(shape=(2049, 12288,))
    for file in os.listdir(dir):
        animal = file.split("_")[0]
        images = []
        for i in os.listdir(dir + "/" + file):
            filename = dir + "/" + file + "/" + i
            image = Image.open(filename)
            images.append(get_data_from(image))

        x_train, x_test, y_train, y_test = get_test_train(images, animal)

        np.concatenate((master_x_train, x_train))
        np.concatenate((master_x_test, x_test))
        np.concatenate((master_y_train, y_train))
        np.concatenate((master_y_test, y_test))

        # master_x_test += x_test
        # master_y_train += y_train
        # master_y_test += y_test

    return (master_x_train, master_x_test), (master_y_train, master_y_test)


if __name__ == "__main__":
    get_all_splits()