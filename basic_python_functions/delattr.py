#delete attribute from object

class MyClass:
    def __init__(self, x):
        self.x = x

c = MyClass(10)

print (c.x)
delattr(c, "x")
try:
    print (c.x)
except AttributeError:
    print ("ERROR DE ATRIBUTO")
c.x = 12
print (c.x)

#equivalente a 

del c.x

try:
    print (c.x)
except AttributeError:
    print ("ERROR DE ATRIBUTO")
