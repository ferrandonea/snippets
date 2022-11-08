#ayuda a mapear valores en una secuencia usando una funcion

vals = [1,2,3,4,5,6,7,8,9,10]

squares = map(lambda x: x **2, vals)
print (list(squares))

items = {"A":1, "B":2, "C":4}
strings = map(lambda key:items[key]*key, items)
print (list(strings))

def  por_dos(x):
    return x*2

print (list(map(por_dos, vals)))