import numpy as np
from functools import reduce

ref = np.array([1,1,1,1])
shoulder = np.transpose(np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 2], [0, 0, 0, 1]]))
elbow = np.transpose(np.array([[0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 1, 2], [0, 0, 0, 1]]))
wrist = np.transpose(np.array([[1, 0, 0, 0], [0, 0.707, 0.707, 0], [0, 0.707, 0.707, 0], [0, 0, 0, 1]]))

print(ref.dot(shoulder).dot(elbow).dot(wrist))

# similarly
ans = [ref, shoulder, elbow, wrist]
print(reduce(lambda x,y: x.dot(y), ans))
