from numpy import *

# Mengunakan tupel Array
# print(zeros((2,3)))
# print(ones((2,3)))

data = ones(4, dtype=int64)
print(data.dtype)

x1 = 5.4 * ones(10)
x2 = full(10, 5.4)
x1 = empty(5)
x1.fill(3.0)
print(x1)
x2 = full(5, 3.0)
print(x2)

# Arrays Filled with Incremental Sequences
#  value index pertama di mulai selalu dari 0
nilai = arange(2, 11 ,1) # 2 = star ,11 = panjang index jadi 0 - 10 (11 index) , 2 = loncatanua +2
print(nilai)

nilaiA = linspace(0, 12, 4) # 0 = star ,10 = end , 5 = end value dgn panjang index 5 value loncatanya sama rata
print(nilaiA)

print('=' * 100)

nilaiB = logspace(0,2,5)
print(nilaiB)

print('='*100)

# Meshgrid Arrays
x = array((-1,0,1))
y = array((-2,0,2))

X, Y = meshgrid(x,y)
print(X)
print(Y)
nilai = (X+Y) ** 2
print(nilai)
