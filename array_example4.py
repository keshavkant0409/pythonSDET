from numpy import *

arr=array([4,6,7,8,9])
print(arr)
arr=arr+5
print(arr)

arr1=array([14,16,17,1,19])
arr3=arr+arr1

print(arr3)
print(sin(arr3))
print(cos(arr3))
print(log(arr3))
print(sqrt(arr3))
print(sum(arr3))
print(min(arr3))
print(max(arr3))
print(sort(arr3))
arr4=concatenate([arr1,arr3])
print(arr4,'+++++++++')
print(unique(arr4))

'copy an array'
arr5=arr4
print(arr4)
print(arr5)
print(id(arr4),id(arr5),'++++++++++++++')

'copy array using view(it is a function to copy array at different location and also it is shallow copy i.e if we change value of one array it will change value of other array)'
arr6=arr4.view()
print(arr4,arr6)
print(id(arr4),id(arr6))
arr4[3]=100
print(arr4,arr6,'+++++++++++++')

'copy array using copy(it is a function to copy array at different location and also it is deep copy i.e if we change value of one array it will not change value of other array)'
arr7=arr4.copy()
print(arr4,arr7)
print(id(arr4),id(arr7))
arr4[5]=2100
print(arr4,arr7)