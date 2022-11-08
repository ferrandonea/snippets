#atributos de parent

class Parent:
    def __init__(self,x) -> None:
        self.x = x
        
    def func(self):
        print ("Parent function")
        
class Child(Parent):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y
        
    def func(self):
        print ("Child function")
        
    def call_parent(self):
        self.func()
        super().func()
        
c = Child(1,2)
c.func()
c.call_parent()