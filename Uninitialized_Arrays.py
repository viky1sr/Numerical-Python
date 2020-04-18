from numpy import *

# def f(x):
#     y = ones_like(x) # menghitung x dgn y
#     return y
#
# print(identity)

# Creating Matrix Arrays

# diagonal = identity(4)
# print(diagonal)

# x = eye(3, k=1)
# print(x)
# y = eye(3, k=-1)
# print(y)

cons = diag(arange(0, 20, 5)) #mulai dari 0 + 5 > 20
print(cons) # diagonal 0 + 5 = 5 + 5 = 10 + 5 = 15 > 20 tidak boleh lebih dari 20 , di karenakan 15 + 5 = 20 tidak boleh > 20 bukan >= 20

