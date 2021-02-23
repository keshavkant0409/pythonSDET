from numpy import *
from numpy.core import linspace

arr=array([1,5,7,8])

'''
to work with multi dimension array in python
we used third party packagenumpy
'''
print(arr)
print(arr.dtype)

'iplicit conversion'
arr1=array([1,5,7,8.0])
print(arr1.dtype)

'assigning type to array'
arr2=array([1,5,7,8.0],int)
print(arr2.dtype)



'linspace(it has 3 parameter 1.start 2.end_includeed 3.numberofparts and 3rd one is optional if it is not defined then it will divide in 50 equal parts) for array'

arr3 = linspace(0,15,16)
print(arr3)


'arange (it has 3 parameter 1.start 2.end_excluded 3.range and 3rd one is optional if it is not defined then range will be 1)'
arr4 = arange(0,15,3)
print(arr4)

'logspace'
arr5 = logspace(1,40,5)
print(arr5)
print('%.2f.'%arr5[4])

'Zeros'
arr6 = zeros(5)
arr7 = zeros(5,int)
print(arr6)
print(arr7)


'ones'
arr8 = ones(5)
arr9 = ones(5,int)
print(arr8)
print(arr9)
