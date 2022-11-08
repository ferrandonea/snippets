#inmutable of set

lst = [1,2,3]
s = set(lst)
s.add(4)
print (s)

fs = frozenset(lst)
print (fs)
#no es mutable, no se puede cambiar y se puede usar como key para un diccionario, es un hashable type