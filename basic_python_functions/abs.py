class ImplementAbs:
    def __init__(self, string):
        self.string = string
    
    def __abs__(self):
        #esta es la implementción
        return self.string.lower()
    
custom_obj = ImplementAbs("HELLO")
 
x = abs(9) #positive
y = abs(-100.876) #positive
z = abs(custom_obj) #custom implementation of abs

print (x,y,z)