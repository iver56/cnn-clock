from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense


def get_cnn_model(num_color_channels, img_width, img_height):
    model = Sequential()
    model.add(
        Convolution2D(
            32,  # nb_filter: Number of convolution kernels to use (dimensionality of the output)
            3,  # nb_row: Number of rows in the convolution kernel
            3,  # nb_col: Number of columns in the convolution kernel
            input_shape=(num_color_channels, img_width, img_height)
        )
    )
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Convolution2D(32, 3, 3))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Convolution2D(64, 3, 3))
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
    return model


def get_ann_model(num_color_channels, img_width, img_height):
    model = Sequential()
    model.add(Flatten(input_shape=(num_color_channels, img_width, img_height)))
    model.add(Dense(12 + 60 + 60))
    model.add(Activation('sigmoid'))

    model.compile(
        loss='binary_crossentropy',
        optimizer='rmsprop',
        metrics=['accuracy']
    )
    return model
