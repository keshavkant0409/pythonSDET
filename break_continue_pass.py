'''
break
example
'''
av=5

x=int(input("enter the num"))
i=1
while i<=x:
    if i>av:
        print()
        print("requirement is high")
        break
    else:
        print("candy",end=' ')
        i+=1

print()
print('bye')

'''
continue
example
'''
print('\ncontinue example')
for i in range(1,x):
    if i%3==0 or i%5==0:
        print(i,end=' ')
    else:
        continue


'''
pass
example......it is use to skip any block or function
'''

print("\npass  example")
for i in range(1,x):
    if i%2!=0:
        pass
    else:
        print(i,end=' ')