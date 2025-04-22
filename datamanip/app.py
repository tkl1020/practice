import numpy as np

# from a list
array = np.array([1,2,3,4])
print(array)

# 2d array
mat = np.array([[1,2],[3,4]])
print(mat)

array = array * 3.14159265
print(array)
mean = np.mean(array)
print("The mean is " + str(mean))
sum = np.sum(array)
print("The sum is " + str(sum))