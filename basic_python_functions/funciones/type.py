x = 1
print(type(x))


def func():
    pass


print(type(func))

# esto es avanzado y un poco absurdo creo
# esto es una forma muy enredada para crear una clase

ClassName = type("ClassName", (object, ), {
                 "attribute": "i am an attribute", "add1": lambda self, x: x+1})

c = ClassName()
print (c.attribute)
print (c.add1(2))
