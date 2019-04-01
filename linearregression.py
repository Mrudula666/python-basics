import numpy as np
import torch


#taking the x and y values for regression
x_values = [i for i in range(11)]
print(x_values)

# Convert to numpy
x_train = np.array(x_values, dtype=np.float32)
print(x_train.shape)
x_train.reshape(-1,1)
x_train.shape

#y_values
y_values = [2*i + 1 for i in x_values]
print(y_values)

#creating the model


