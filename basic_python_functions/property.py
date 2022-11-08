#returns a property attribute

class C:
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x if self._x != None else 1
    
    def setx(self, value):
       self._x = round(value)
    
    def delx(self):
        del self._x
        
    x = property(getx, setx, delx, "I'm the x property") 
    
var = C()
print (var.x)
var.x = 10.2
print (var.x)

#equivalente y preferible
class C2:
    def __init__(self):
        self._x = None
    
    @property
    def x(self):
        """I'm, the x property"""
        return self._x
    
    @x.setter
    def x(self, value):
        self._x = round(value)
        
    @x.deleter
    def x(self):
        del self._x
    
    @x.getter
    def x(self):
        return self._x if self._x != None else 1
    
var = C2()
print (var.x)
var.x = 10.2
print (var.x)
