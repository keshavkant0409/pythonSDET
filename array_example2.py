from array import *

arr=array('i',[])

len_arr=int(input('length of the array'))

for i in range(len_arr):
    x=int(input('enter the value'))
    arr.append(x)


print(arr)

val=int(input('enter the number for search'))

k=0
for i in arr:
    if i==val:
        print(k)
        break
    k+=1

print(arr.index(val))