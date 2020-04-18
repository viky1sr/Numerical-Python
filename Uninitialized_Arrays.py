from numpy import *

# def f(x):
#     y = ones_like(x) # menghitung x dgn y
#     return y
#
# print(identity)

# Creating Matrix Arrays

diagonal = identity(4)
print(diagonal)

x = eye(3, k=1)
print(x)
y = eye(3, k=-1)
print(y)

cons = diag(arange(0, 20, 5)) #mulai dari 0 + 5 > 20
print(cons) # diagonal 0 + 5 = 5 + 5 = 10 + 5 = 15 > 20 tidak boleh lebih dari 20 , di karenakan 15 + 5 = 20 tidak boleh > 20 bukan >= 20
print('='*100)

#    CATATAN ( DESKRIPSI)

# a[m] Select element at index m, where m is an integer (start counting form 0).
# a[-m] Select the n th element from the end of the list, where n is an integer. The last
# element in the list is addressed as –1, the second to last element as –2, and so on.
# a[m:n] Select elements with index starting at m and ending at n − 1 (m and n are integers).
# a[:] or
# a[0:-1]
# Select all elements in the given axis.
# a[:n] Select elements starting with index 0 and going up to index n − 1 (integer).
# a[m:] or
# a[m:-1]
# Select elements starting with index m (integer) and going up to the last element in
# the array.
# a[m:n:p] Select elements with index m through n (exclusive), with increment p.
# a[::-1] Select all the elements, in reverse order

a = arange(0,11) # 0 mulai index , 11 last index , index selalu di muali dari 0
print(a)
print(a[1:-1])
print(a[1:-1:2])
print(a[:5]) # jika nilai di kasi - (min) maka index yg bernial 5  di print (di karenakan ini n )
print(a[-5:]) # jika nilai di kasi - (min) maka index yg bernial 5 tidak di print (di karenakan ini m )
print(a[::-2]) # jika 2 ( p ) adalah - (min) maka di index pertama value na adalah value terakhir (n) jika + (plush) valuna na (m)

print('='*100)

# Multidimensional Arrays

# m = mulai (start) , n = akhir (finish)

f = lambda m, n: n + 10 * m # 10 adalah next colum selalu mulai dari 10++ ( 10 , 20 ,30 dan seterus na )
A = fromfunction(f , (6,6), dtype=int) # matrix 6x6 ( kolum 6x6 )
# print(A)
print(A[:, 1]) # colum pertama yg index na di mulai dari index 1
print(A[1, :]) # di ambil dari row ke 1 ( row di pyton sama seperti index di mulai dari 0 )
print(A[:4, :3]) # matrix 4 x 3 di karenakan [:4 , :3]  , di ambil sampai row ke 4 krn :4 ,dan di ambil hanya 3 index saja krn :3
print(A[4:, 3:]) # di ambil dari row paling akhir
print(A[::2, ::2]) # di mulai dari 0,0 , row ke 0 + 2 ++ , index ke 0 + 2 ++
print(A[1::2, 1::3]) # dimuali dari 1,1 . 1::2 di mulai dari row 1 + 2 ++ , 1::3 di muali dari index  1 + 3 = max index sampai 4

# Views
# Subarrays that are extracted from arrays using slice operations are alternative views of the same underlying array data.

B = A[1:5, 1:5] # 1:5 (m) di mulai dari row ke 1 sampai ke 5 , 1:5 (n) di muali dari index ke 1 dan sampai index ke 5
print(B)#kamu harus ingat ( index or row ) selalu mulai dari 0
B[:, :] = 8 # mengisi nilai full pada row pertama dan akhir , dan row selanjutnya bernilai 8 pada index or row 1 sampai sblm terkahir
print(A)

C = B[1:3, 1:3].copy()
print(C)
C[:,:] = 1 # this does not affect B since C is a copy of the view B[1:3, 1:3]
print(C)
print(B)
# In addition to the copy attribute of the ndarray class, an array can also be copied
# using the function np.copy or, equivalently, using the np.array function with the
# keyword argument copy=True.
