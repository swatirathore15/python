from numpy import *
num1 = array([
                [1, 2, 3, 7, 8, 9],
                [4, 5, 6, 0, 1, 2]
            ])

print(num1)
print(id(num1))
print(num1.dtype)
print(num1.size)
print(num1.ndim)
print(num1.shape)

num2 = num1.flatten()
print(num2)

#num3 = num2.reshape(2, 3)
#print(num3)

num3 = num2.reshape(2, 2, 3)
print(num3)