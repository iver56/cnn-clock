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

from keras import backend as keras_backend
from representation import *
import models


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

model = models.get_ann_model(num_color_channels, img_width, img_height)
print(model.summary())

model.fit(
    x_train,
    y_train,
    batch_size=32,
    nb_epoch=300
)

model.save('clock.h5')
