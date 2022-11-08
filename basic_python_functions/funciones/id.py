# identifier de un objeto, sirve para saber si dos objetos son lo mismo

x = [1, 2, 3]
y = x
a = 1000000
b = a+1-1

print (id(x))
print (id(y))
print ()
print (id(a))
print (id(b))

y.append(4) #porque y es un alias de x
print (x)