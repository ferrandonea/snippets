class Pet:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self) -> str:
        return f"Pet(name={self.name})"

p = Pet("Billy")

p2 = Pet("Sally")

print (p)
print (repr(p))
print (repr(p2))
    