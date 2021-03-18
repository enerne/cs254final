import get_data
import numpy as np

x_train: np.array
(x_train, x_test), (y_train, y_test) = get_data.get_all_splits()

o = x_train[0]
print(type(o))
print(o.shape)
print(o)

# ok at this point we have lists in the proper formats, we can implement the algorithm now