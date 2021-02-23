'a and b is formal argument'
def add(a,b):
    c=a+b
    print(c)
'5 and 6 is actual argument'
add(5,6)

'actual argument is of 4 types : 1)position 2) keyword 3)Default 4)variable length'

'eg of position argument function'

def person(name,age):
    print(name,age)

person('keshav',25)

'eg of keyword argument function'

def person(name,age):
    print(name,age)
    c=age-5
    print(c)

person(age=25,name='keshav')

'eg of default argument function'

def person(name,age=25):
    print(name,age)
'here age is not passed hence it is taking the default 25'
person(name='keshav')


def person(name, age=25):
    print(name, age)

'here age is passed hence it is updating the  the default age to actual age i.e 26'
person('keshav',26)


'eg of variable length argument function'

def add(a,*b):
    c=a
    'b is tuple so we can not add a and b....to add and b we fetch value from b one by one'
    for i in b:
        c=c+i
    print(c)

add(23,34,56,78)

def add(*b):
    c=0

    for i in b:
        c=c+i
    print(c)

add(23,34,56,78)

