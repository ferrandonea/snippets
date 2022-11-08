#un static method does not have access
#to the class o the instance, es una utility function

class Helpers:
    @staticmethod
    def add(x,y):
        return x+y
    
_sum = Helpers.add(1,2)
print (_sum)

h = Helpers()
_sum2 = h.add(2,3)
print (_sum2)