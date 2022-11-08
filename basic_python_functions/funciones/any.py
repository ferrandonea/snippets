# any objects in a iterator are true

a = [1, 0, 1, 2, 3]
print(any(a))  # True

b = [True, True, 1, 2]
print(any(b)) #True

c = ["", "a", "b"]
print(any(c))  # True

d = [[0, 0], [0, 0], [0, 0]]
print(any(d)) #True

e = [[], [1], True]
print(any(e)) # True

f = [[], 0, False]
print(any(f)) # False porque todos son falsos