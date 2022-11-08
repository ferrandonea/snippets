#ve si algo es callable --> call it like a function

class Class:
    pass

def func():
    print ("Hi")

def func2():
    def inner():
        pass
    return inner

func3 = lambda x: x+1
not_func = "Hello"

print (callable(Class)) #True
print (callable(func)) #True
print (callable(func())) #False (el resultado no es callable)
print (callable(func2())) #True (el resultado es una funcion)
print (callable(func3)) #True
print (callable(not_func)) #False