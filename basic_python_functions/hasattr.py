#si tiene atributo especifico, para evitar un try/except
class MyClass:
    def __init__(self, x):
        self.x = x
        
c = MyClass(10)
print (hasattr(c,"x"))
print (hasattr(c,"y"))