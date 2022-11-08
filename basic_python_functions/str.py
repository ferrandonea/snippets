#return string representation of an object

class Obj:
    def __init__(self, x) -> None:
        self.x = x
    def __str__(self) -> str:
        return f"Obj({self.x})"

lst = ["1","2", "a", "b", "d"]
print (lst)
print (str(lst))

num = 4
print (str(num))

s = {4,4,2,1,3,6,"hi"}
print (str(s))
o = Obj(2)
print (str(o))