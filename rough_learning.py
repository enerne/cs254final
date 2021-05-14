import get_data
import numpy as np
from sklearn.tree import DecisionTreeClassifier

x_train: np.array
(x_train, x_test), (y_train, y_test) = get_data.get_all_splits()

o = x_train[0]
print(type(o))
print(o.shape)
print(o)

# ok at this point we have lists in the proper formats, we can implement the algorithm now
tree = DecisionTreeClassifier()
print(type(tree), type(x_train), type(y_train), x_train.shape, y_train.shape)
tree.fit(x_train, y_train)
accuracy = tree.score(x_test, y_test)
print(accuracy)
