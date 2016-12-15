import numpy as np
import math

def mag(v):
    return np.linalg.norm(v)

def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0:
       return v
    return v / norm

q2a = np.array([4,3])
q2b = np.array([2,-3])
q2c = np.array([5,15])
q2d = np.array([5,1])

print(mag(q2a), mag(q2b), mag(q2c), mag(q2d))

q3 = [np.array([4,3]), np.array([7,3]), np.array([-4,8]), np.array([10,-15])]

print(list(normalize(arr) for arr in q3))

def dotproduct(v1, v2):
    return sum((a*b) for a, b in zip(v1, v2))

def angle(v1, v2):
    return math.acos(dotproduct(v1, v2) / (mag(v1) * mag(v2)))

#print(angle(np.array([8,5]), np.array([14,3])) * 180 / math.pi)

print(angle(np.array([1,2,8]), np.array([3,6,4])) * 180 / math.pi)
