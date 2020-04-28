from numpy import *

# Fancy Indexing and Boolean-Valued Indexing

A = linspace(0, 1, 11)
print(A)
print(A[array([0,2,4])]) # mencari nilai 0 2 4
print(A[[0,2,4]]) # The same thing can be accomplished by indexing with a Python list

# NumPy array and indexing using a Boolean-valued array

print(A > 0.5)
print(A[A > 0.5])

# Unlike arrays created by using slices, the arrays returned using fancy indexing and
# Boolean-valued indexing are not views but rather new independent arrays. Nonetheless,
# it is possible to assign values to elements selected using fancy indexing:

A = arange(10)
indices = [2, 4, 6] # indices mengubah nilai pada index [2 4 6]
B = A[indices]
B[0] = -1 # tidak mempengaruhin nilai Vairable A
print(A)
A[indices] = -1 # ini mengubah nilai Variable A
print(A)

print('='*100)

# and likewise for Boolean-valued indexing:
A = arange(10)
B = A[A > 5]
B[0] = -1
print(A)
A[A > 5] = -1 # jika A (index) > 5 (index) makan nilai index selanjutnya -1
print(A)

# Reshaping and Resizing
# Summary of NumPy Functions for Manipulating the Dimensions and the Shape of Arrays
"""
Function/Method         ||  Description
np.reshape              ||  Reshape an N-dimensional array. The total number of elements must  
np.ndarray.reshape      ||  remain the same.
np.ndarray.flatten      ||  Creates a copy of an N-dimensional array, and reinterpret it as a one-dimensional array (i.e., all dimensions are collapsed into one). 
np.ravel                ||  Create a view (if possible, otherwise a copy) of an N-dimensional array 
np.ndarray.ravel        ||  in which it is interpreted as a one-dimensional array
np.squeeze              ||  Removes axes with length 1.
np.expand_dims,         ||  Add a new axis (dimension) of length 1 to an array, where np
np.newaxis              ||  newaxis is used with array indexing.
np.transpose            ||  Transpose the array. The transpose operation corresponds to reversing (or more generally, permuting) the axes of the array.
np.ndarray.transpose    ||  
np.ndarray.T            ||
np.hstack               ||  Stacks a list of arrays horizontally (along axis 1): for example, given a list of column vectors, appends the columns to form a matrix.
np.vstack               ||  Stacks a list of arrays vertically (along axis 0): for example, given a list of row vectors, appends the rows to form a matrix.
np.dstack               ||  Stacks arrays depth-wise (along axis 2).
np.concatenate          ||  Creates a new array by appending arrays after each other, along a given axis.
np.resize               ||  Resizes an array. Creates a new copy of the original array, with the
                            requested size. If necessary, the original array will be repeated to fill
                            up the new array.
np.append               ||  Appends an element to an array. Creates a new copy of the array
np.insert               ||  Inserts a new element at a given position. Creates a new copy of the array
np.delete               ||  Deletes an element at a given position. Creates a new copy of the array.
"""

# Reshaping
# data = array([[1,2] , [3,4]]) or bisa menggunakan matrix('1,2; 3,4')
data = matrix('1,2; 3,4')
print(data)
print(reshape(data, (1,4)))
print(data.reshape(4))

data = array([[1, 2], [3, 4]])
print(data.flatten())
print(data.flatten().shape)

data = arange(0,5)
colum = data[:, newaxis]
print(colum)
row = data[newaxis, :]
print(row)

print('='*100)

data = arange(5)
print(data)
print(vstack((data,data,data))) # vstack = vertically
print(hstack((data,data,data))) # hstack = horizontally

data = data[:, newaxis]
print(hstack((data, data, data)))



# Arithmetic Operations

x = array([1, 2, 3, 4]).reshape(2, 2) # reshape akan membuat matrix 2 x 2
z = array([[1, 2]]) # matrix bisa mengunakan resahpe or list -> [[ ]] 2x

print(x/z) # matirx 2x2 / 1x2 = x /z ( 1:1 = 1 , 3:1 = 3 , 2:2 =1 , 4:2 = 2)
zz = concatenate([z,z], axis=0) # axis=0 unutk membuat matrix 2,2 dan axis=1 untuk membuat 1x4
print(zz) # matrix (2,2) karena mengunakan concatenante

z = array([[1], [2]])
zz = concatenate([z,z], axis=1) # membuat menjadi 2 di mensi yg sama dengan x tetapi valuna berbeda
print(zz) # fungsi axis=1 untuk menduplikatin value tersebut jadi ([1,1] [2,2])

""" 
Operator    ||      Operation
+, +=               Addition
-, -=               Subtraction
*, *=               Multiplication
/, /=               Division
//, //=             Integer Division
**, **=             Exponentiation
 
 """
