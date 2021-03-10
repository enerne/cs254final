import numpy
import matplotlib.pyplot as plt
import os
from PIL import Image

sizes = []
for filename in os.listdir("data/test/"):
    try:
        i = Image.open("data/test/" + filename)
        sizes.append(i.size)
    except FileNotFoundError:
        print("error")

sizes = numpy.ndarray(sizes)
plt.scatter(sizes[0], sizes[1], s=75, c=T, alpha=.5)