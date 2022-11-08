key = "randomstring"
print (hash(key))

num_hash = hash((1,2))
print (num_hash)

diccionario = {"a":1, "b":2}
print (hash(str(diccionario)))

diccionario = {"a":1, "b":2}
print (hash(diccionario)) #falla

# no se puede hacer hash de una lista , set, diccionario, pero si un tuple