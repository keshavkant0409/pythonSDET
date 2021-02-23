from array import *

vals=array('i',[5,7,8,9,0,-9])

print(vals)


print(vals.buffer_info())

vals.reverse()

print(vals)

for i in range(len(vals)):
    print(vals[i],end=' ')
print()
for i in vals:
    print(i,end=' ')

newarr=array(vals.typecode,(a for a in vals))
print()
for i in newarr:
    print(i,end=' ')

    
newarr1=array(vals.typecode,(a*a for a in vals))
print()
for i in newarr1:
    print(i,end=' ')

