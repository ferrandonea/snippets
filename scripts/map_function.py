# map
# looping without a loop
# map function calls to a collection of items
#map(fun, iterable)

# basic usage - count len
people = ["Matt", "Bryan", "Tammy", "Markus"]

# old way
counts = []
for x in people:
    counts.append(len(x))

print(f'Old way: {counts}')

# modern way
print(f'Modern way: {list(map(len, people))}')

# now we are going to combine elements
# note that are different sizes, we are also passing multiple args

firstnames = ["Apple", "Chocolate", "Fudge", "Pizza"]
lastnames = ["Pie", "Cake", "Brownies"]


def merge(a, b):
    return a + ' ' + b


x = map(merge, firstnames, lastnames)
print(x)
# this print a map object
print(list(x))

# multiple functions , combine functions in one map call


def add(a, b):
    return a+b


def substract(a, b):
    return a-b


def divide(a, b):
    return a/b


def multiply(a, b):
    return a*b


def doall(func, num):
    """[summary]

    Args:
        func ([def]): Function
        num ([list]): of numbers
    """
    return func(num[0], num[1])


# tuple of functions
f = (add, substract, multiply, divide)
v = [[5, 3]]  # list inside of a list
n = list(v)*len(f)
print (n)
# has 4 items
m = map(doall, f, n)
print (list(m))
