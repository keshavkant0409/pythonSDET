def count(lst):
    even=0
    odd=0

    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd


lst=[12,23,32,34,45,56,67,78,89,9,4,5,6,8,2,]
even,odd=count(lst)
print('even:{} and odd:{}'.format(even,odd))