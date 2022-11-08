import pickle

def outline(func):
    def inner(*args, **kwargs):
        print("INICIO FUNCION")
        print(f"Function : {func.__name__}")
        func(*args, **kwargs)
        print("FIN FUNCION")
    return inner


class Cat:
    def __init__(self, name, age, info):
        self._name = name
        self._age = age
        self._info = info

    @outline
    def display(self, msg=''):
        print(msg)
        print(f"{self._name} is a {self._age} years old cat")
        for k, v in self._info.items():
            print(f'\t{k} = {v}')


othello = Cat("Othello", 15, dict(color='Black', weight=15, loves="eating"))
othello.display("Testing")

#serializa
sc = pickle.dumps(othello)
print (sc)

with open('cat.txt', 'wb') as f:
    pickle.dump(othello, f)

#deserialize

mycat = pickle.loads(sc)
print (f'from string')
mycat.display("from string")

with open('cat.txt', 'rb') as f:
    diskcat = pickle.load(f)
diskcat.display("from disk")

print (mycat)
print (diskcat)