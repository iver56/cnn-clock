from representation import *
from keras.models import load_model
import os
from keras import backend as keras_backend

keras_backend.set_image_dim_ordering('th')


model = load_model('clock.h5')


image_dir = os.path.join('data', 'validation')
x_validation, y_validation = get_images(image_dir)

print type(x_validation)
print type(y_validation)


for i in range(len(x_validation)):
    x_sample = x_validation[i]
    y_true = y_validation[i]

    true_time = interpret_y_vector(y_true)

    y_predicted = model.predict_proba(
        np.array([x_sample]),
        verbose=0
    )[0]

    predicted_time = interpret_y_vector(y_predicted)
    print 'true time: {0}, estimated time: {1}'.format(
        str(true_time).ljust(12),
        str(predicted_time).ljust(12)
    )
