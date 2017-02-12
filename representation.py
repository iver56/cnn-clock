from skimage.io import imread
import numpy as np
import os


def vectorize_y(hour, minute, second):
    vector = np.zeros(12 + 60 + 60)
    vector[hour] = 1
    vector[12 + minute] = 1
    vector[12 + 60 + second] = 1
    return vector


def interpret_y_vector(vector):
    hour_vector = vector[:12]
    hour = np.argmax(hour_vector)

    minute_vector = vector[12:12 + 60]
    minute = np.argmax(minute_vector)

    second_vector = vector[12 + 60:]
    second = np.argmax(second_vector)

    return hour, minute, second


def rescale_image(image):
    return image / 255.0


def get_images(path):
    x = []
    y = []
    for root, dirs, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith('.png'):
                file_path = os.path.join(path, filename)
                image = imread(file_path, as_grey=True)
                x.append(image)
                filename = filename.replace('.png', '').replace('clock_', '')
                hour, minute, second = map(int, filename.split('_'))
                vector_y = vectorize_y(hour, minute, second)
                y.append(vector_y)
        break  # no recursive walk
    x = np.array(x)
    x = x.reshape(
        (
            x.shape[0],  # number of samples
            1,  # number of color channels (1 means greyscale)
            x.shape[-2],  # image width
            x.shape[-1]  # image height
        )
    )
    y = np.array(y)
    return x, y
