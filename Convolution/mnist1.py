import tensorflow as tf

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

print(x_train.shape, y_train.shape)

print(x_test.shape, y_test.shape)


import matplotlib.pyplot as plt

image_index = 7777  # You may select anything up to 60,000
print(y_train[image_index])  # The label is 8
print(x_train[image_index].shape)
plt.imshow(x_train[image_index], cmap='Greys')
plt.show()
