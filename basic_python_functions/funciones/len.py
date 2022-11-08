#llama el metodo  __len__
class Custom:
    def __len__(self):
        return 5


c = Custom()
print(len(c))

x = [1, 2, 3, 4]
print(len(x))

y = "string"
print(len(y))

items = {1: 1, 2: 2, 3: 3}
print(len(items))

s = set([1, 2, 3])
print(len(s))
