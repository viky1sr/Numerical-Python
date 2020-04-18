from numpy import *

print(array([1,2,3], dtype=int))
print(array([1,2,3], dtype=float))
print(array([1,2,3], dtype=complex))

print('='*100)

# numpy array
# jenisnya tidak dapat diubah, selain dengan membuat
# salinan baru dengan nilai array yang di copy

data = array([1,2,3], dtype=float)
print(data)
print(data.dtype)
# or by using the astype method of the ndarray class:
print(data.astype(int))

print('='*100)

data = array([1,2,3], dtype=int)
print(data)
print(data.dtype)

print('='*100)

# adding float-valued and  complex-valued arrays,
# the resulting array is a complex-valued array

d1 = array([1,2,3], dtype=float)
d2 = array([1,2,3], dtype=complex)
print(d1+d2)
print((d1+d2).dtype)

print('-'*100)
# In some cases, depending on the application and its requirements, it is essential to
# create arrays with data type appropriately set to, for example, int or complex. The default
# type is float

print(sqrt(array([-1,0,1])))
print(sqrt(array([-1,0,1], dtype=complex)))
# RuntimeWarning: invalid value encountered in sqrt
#  array([ nan, 0., 1.])
# warning jika tidak mengunakan dtype=complex

print('-'*100)
# Real and Imaginary Parts
# Regardless of the value of the dtype attribute, all NumPy array instances have the attributes
# real and imag for extracting the real and imaginary parts of the array, respectively

data = array([1,2,3], dtype=complex)
print(data)
print(data.real) #real is 1
print(data.imag) #img is 0