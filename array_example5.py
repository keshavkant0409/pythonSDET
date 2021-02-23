'matrix or multi dimension array'
from numpy import *

arr=array([

    [1,3,5,4,8,4],[5,90,7,8,9,78]
])

print(arr)
print(arr.dtype)
print(arr.ndim)
print(arr.shape)
print(arr.size)
arr2=arr.flatten()
print(arr2)
arr3=arr2.reshape(4,3)
print(arr3)
arr4=arr2.reshape(3,2,2)
print(arr4,'+++++++++++++')

m=matrix('1 4 5 ; 3 5 8 ; 5 8 6')
print(m,'++++++++')
print(diagonal(m))
print(m.min())
m2=matrix('1 4 15 ; 13 5 8 ; 15 18 6')
print(m+m2,'addition')
print(m*m2,'multiplication')