from PIL import Image
import os
import constants

path = "data/test/"
files = os.listdir("data/test/")


# function takes a string for the relative path to the image, and an optional tuple denoting size.
# the default is 64x64 because that's what we'll be using the most (at the beginning at least)
def load_image_with_size(image_path, size=(64, 64)):
    image = Image.open(image_path)
    image = image.resize(size)
    return image


def resize_directory(directory, output):
    print("make", output + directory)
    os.mkdir((output + directory)[:-1])
    for file in os.listdir(directory):
        if not file.endswith(".txt"):
            im = load_image_with_size(directory + file)
            im.save(output + directory + file)


def resize_all_images():
    resize_directory("data/test/", "output/")
    os.mkdir("output/data/train")
    for directory in os.listdir("data/train/"):
        resize_directory("data/train/" + directory + "/", "output/")


if __name__ == "__main__":
    resize_all_images()

# for i in range(1):
#     filename = files[i]
#     img = load_image_with_size(path + filename)
#     # img = Image.open(path + filename)
#     # img = img.resize((64,64))
#     img.save("output/" + filename)
#

