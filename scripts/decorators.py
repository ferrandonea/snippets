# decorators

# everything in python is an object
# even functions can be used as objects
# a decorator takes in a function, adds some functionality and returns it

# basic decorator
# in this example we will change the execution order

def test_decorator(func):
    print('before')
    func()
    print('after')


@test_decorator
def do_stuff():
    print("Doing stuff")

# THIS IS NOT CORRECT YOU SHOULD USE AN INNER FUNCTION!!
# that is because the test_decorator in this example is not returning
# something


# now we are going to correct this
print("-="*20)
print("CORRECT WAY")
print("-="*20)


def makeBold(func):
    def inner():
        print('<B>')
        func()
        print('</B>')
    return inner  # Return the inner function


@makeBold
def printName():
    print("Bryan Cairns")

# makeBold(printName) ==> ESO ES LO QUE HACE


printName()

# We want to pass parameters
# Notice this has a defined number of params


def divide(a, b):
    print(a/b)

# divide(100,3)
# divide(100,0)
# divide(100,'cat')

#we need a decorator to check if we can even do the division

def numcheck(func):
    def checkInt(o):
        if isinstance(o,int):
            if o == 0:
                print ("Can not divide by zero")
                return False
            return True
        print (f"{o} is not a number")
        return False

    def inner(x,y):
        #we are matching the function call (x,y)
        if not checkInt(x) or not checkInt(y):
            return #takes no action
        return func(x,y)
    return inner

@numcheck
def division(a,b):
    print(a/b)

division(100,3)
division(100,0)
division(100,'cat')
