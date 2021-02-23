def update(x):
    x=8
    print(x)
update(10)


def update(x):
    x=8
    print(x)
a=10
update(a)
print(a)


def update(x):
    print(id(x))
    x=8
    print(id(x))
    print(x)
a=10
print(id(a))
update(a)
print(a)

def update(lst):
    print(id(lst))
    lst[1]=-8
    print(id(lst))
    print(lst)
'list is mutable...hence value get updated in original list also'
lst=[10,56,78]
print(id(lst))
update(lst)
print(lst)