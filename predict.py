from __future__ import division
from representation import *
from keras.models import load_model
import os
from keras import backend as keras_backend

keras_backend.set_image_dim_ordering('th')

model = load_model('clock.h5')

image_dir = os.path.join('data', 'validation')
x_validation, y_validation = get_images(image_dir)

print(type(x_validation))
print(type(y_validation))

hour_matches = 0
minute_matches = 0
second_matches = 0
exact_matches = 0

for i in range(len(x_validation)):
    x_sample = x_validation[i]
    y_true = y_validation[i]

    true_time = interpret_y_vector(y_true)

    y_predicted = model.predict_proba(
        np.array([x_sample]),
        verbose=0
    )[0]

    predicted_time = interpret_y_vector(y_predicted)
    print(
        'true time: {0}, estimated time: {1}'.format(
            str(true_time).ljust(12),
            str(predicted_time).ljust(12)
        )
    )
    if true_time[0] == predicted_time[0]:
        hour_matches += 1
    if true_time[1] == predicted_time[1]:
        minute_matches += 1
    if true_time[2] == predicted_time[2]:
        second_matches += 1
    if true_time == predicted_time:
        exact_matches += 1

print('Hour matches: {}%'.format(100 * hour_matches / len(x_validation)))
print('Minute matches: {}%'.format(100 * minute_matches / len(x_validation)))
print('Second matches: {}%'.format(100 * second_matches / len(x_validation)))
print('Exact matches: {}%'.format(100 * exact_matches / len(x_validation)))
