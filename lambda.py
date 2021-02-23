f=lambda a:a*a

result=f(5)
print(result)


f=lambda a,b:a+b

result=f(5,6)
print(result)


nums=[6,7,8,9,5,56,76,54,45,43]

evens=list(filter(lambda n:n%2==0,nums))
print(evens)