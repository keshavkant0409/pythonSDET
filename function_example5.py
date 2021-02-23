'Global variable'

a=10

def something():
    a=8
    print('in side function',a)

something()
print('outside side function',a)


'update Global variable'

a=10

def something():
    'explicitly call global variable'
    global a
    a=8
    print('in side function',a)

something()
print('outside side function',a)


'update Global variable and use same variable name inside the function'

a=10
b=23
print(id(a))
def something():
    a=9
    'store address of all global variable using globals'
    x=globals()['a']
    print(id(x))
    globals()['a']=15

    print('hello in side function',a)

something()
print('hello outside side function',a)