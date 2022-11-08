#open a new file 

# modos
# r reading
# w writing
# x creación, falla si archivo existe
# b modo binario
# t modo texto
# a appending
# + updating (lee y escribe)

import json

f = open("len.py", "r")
lines = f.readlines()
print (lines)
f.close()

with open('len.py', 'r') as f:
    lines = f.readlines()
    print (lines)

data = {"tim": "is the best"}

with open('data.json','w') as f:
    json.dump(data, f)