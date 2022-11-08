import enum


values = ["a", "b", "c", "d", "e"]

for index, value in enumerate(values):
    print (f"{index}: {value}")
    
print (list(enumerate(values))) #lista de tuplas [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')]