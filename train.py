"""
In summary, this is our directory structure:
```
data/
    train/
        clock_4_23_59.png
        (...)
    validation/
        clock_10_21_5.png
        (...)
```
"""

from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as keras_backend
from representation import *


keras_backend.set_image_dim_ordering('th')


train_dir = os.path.join('data', 'train')
x_train, y_train = get_images(train_dir)

validation_dir = os.path.join('data', 'validation')
x_validation, y_validation = get_images(validation_dir)

num_train_samples = len(x_train)
num_validation_samples = len(x_validation)

img_width = img_height = 128
num_color_channels = 1  # 1 means greyscale

print 'num_train_samples', num_train_samples
print 'num_validation_samples', num_validation_samples

model = Sequential()
model.add(
    Convolution2D(
        64,  # nb_filter: Number of convolution kernels to use (dimensionality of the output)
        3,  # nb_row: Number of rows in the convolution kernel
        3,  # nb_col: Number of columns in the convolution kernel
        input_shape=(num_color_channels, img_width, img_height)
    )
)
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Convolution2D(64, 3, 3))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Convolution2D(128, 3, 3))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(12 + 60 + 60))
model.add(Activation('relu'))
model.add(Dropout(0.1))
model.add(Dense(12 + 60 + 60))
model.add(Activation('sigmoid'))

model.compile(
    loss='binary_crossentropy',
    optimizer='rmsprop',
    metrics=['accuracy']
)

model.fit(
    x_train,
    y_train,
    batch_size=32,
    nb_epoch=3
)

model.save('clock.h5')
