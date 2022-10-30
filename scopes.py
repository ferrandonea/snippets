a = 1


def f():
    """
    Usa variable global porque no hay 'a' local
    """
    print('Inside f() : ', a)


def g():
    """
    Variable 'a' se redefine como local
    """
    a = 2
    print('Inside g() : ', a)


def h():
    """
    Modifica global 'a' por keyword global
    """
    global a
    a = 3
    print('Inside h() : ', a)

#si no hubiera puedo 'global'
# daría 
# "UnboundLocalError: local variable 'a' referenced before assignment"


print('global : ', a)
f()
print('global : ', a)
g()
print('global : ', a)
h()
print('global : ', a)

