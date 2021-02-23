
#write in new file: we loose existing data
f=open('abc','w')

f.write("hello")
f.write("keshav")


#read the existing file

f1=open('demo','r')
print(f1)
print(f1.read())   #print entire file
print('##################')
print(f1.readline())  # print first line



#append the existing file: will not loose the existing data
f2=open('abc1','a')
f2.write("abchdggf")
for data in f1:
    f2.write(data)


#read in binary format: it is useful in copying picture

f3=open('image.jpg','rb')

f4=open('mypic1.jpg','wb')
for i in f3:
    f4.write(i)
