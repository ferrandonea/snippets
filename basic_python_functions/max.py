numbers = [0, -9, 8, 6, 0, 2, 34]
print(max(numbers))

print(max(3, 4, 5, 9, -1))

#first element of each list
print(max([1, 2, 3, 4], [1, 2, 4], [2, 1]))

#ascii?
print(max("hello", "world", "yes", "ya"))

class Custom:
    def __init__(self, val):
        self.val = val
        
    def __repr__(self):
        return f"Custom({self.val})"
        
c1 = Custom(1)
c2 = Custom(2)
c3 = Custom(3)

print (max(c1,c2,c3, key=lambda x:x.val))