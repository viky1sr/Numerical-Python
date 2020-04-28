from numpy import *

"""
|---------------------------------------------------------------------------------------------------|
|    NumPy Function                      ||                 Description                             |
|---------------------------------------------------------------------------------------------------|
|   np.cos, np.sin, np.tan                |         Trigonometric functions                         |
|   np.arccos, np.arcsin, np.arctan       |         Inverse trigonometric functions.                |
|   np.cosh, np.sinh, np.tanh             |         Hyperbolic trigonometric functions.             |
|   np.arccosh, np.arcsinh, np.arctanh    |         Inverse hyperbolic trigonometric functions.     |
|   np.sqrt                               |         Square root.                                    |
|   np.exp                                |         Exponential.                                    |
|   np.log, np.log2, np.log10             |         Logarithms of base e, 2, and 10, respectively   |
|---------------------------------------------------------------------------------------------------|

"""

x = linspace(-1,1,11) # mulai dari -1 , dan akhir sampai 1 , dengan jumlah index 11 dgn nilai sama rata
print(x)
y = sin(pi * x)
print(y.round(decimals=2))
