# all objects in a iterator are true

a = [1, 0, 1, 2, 3]
print(all(a))  # False -> 0 is not True value

b = [True, True, 1, 2]
print(all(b)) #True

c = ["", "a", "b"]
print(all(c))  # empty string is false

d = [[0, 0], [0, 0], [0, 0]]
print(all(d)) #True all items in list are True

e = [[], [1], True]
print(all(e)) #empty array is false
