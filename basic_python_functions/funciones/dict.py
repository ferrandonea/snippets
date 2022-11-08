# crea diccionario

lst = [("a", 1), ("b", 2)]
lst_dict = dict(lst)
print (lst_dict)

lst = [["a", 1], ["b", 2]]
lst_dict = dict(lst)
print (lst_dict)

lst = [["a", 1,2], ["b", 2,3]]
try:
    lst_dict = dict(lst)
    print (lst_dict)
except ValueError as e:
    print (e)

lista1 = ["a","b"]
lista2 = [1,2]
print (dict(zip(lista1, lista2)))