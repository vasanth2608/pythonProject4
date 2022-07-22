x = lambda a,b,c : a*b*c
print(x(2,3,6))

x = lambda a : a+10
print(x(5))

def myfunc(n):
    return lambda a: a*n
mytripler =myfunc(3)
mydoubler =myfunc(2)
print(mydoubler(10))
print(mytripler(11))