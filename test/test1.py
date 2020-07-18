import numpy as np

#1 test zip and random 
def call_zip(sizes):
    for x, y in zip(sizes[:-1], sizes[1:]):
        print(x, y)

sizes = [784, 100, 10]
# print(sizes[:-1])
# print(sizes[1:])

#call_zip(sizes)

print(np.random.randn(2, 2))

#2 xrange act like range but it create a xrange object instead of a list in means that element created by the xrange can be modifiable
#carefull in python3 xrange is renamed by range
# print(xrange(1, 100))

#3 numpy

arr = np.array([1, 2, 3, 4])

#shape return the dimension of the array: here is one dimensional array with 4 entries
print(arr.shape)


#4 np.zeros
arr = np.random.randn(2, 2)
print(arr.shape)
print(np.zeros(arr.shape))