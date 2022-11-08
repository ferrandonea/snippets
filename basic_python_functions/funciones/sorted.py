lst = [3,4,22,-9,-2,44,2]
print (sorted(lst))
print (list(sorted(lst)))

print (list(sorted(lst, reverse=True))) #descending

string_ = "aabbbcxxxssjjssaa33#d"
sorted_string = sorted(string_)
print (sorted_string)
print ("".join(sorted_string))

#en diccionario sortea los keys
diccionario = {"a":1, "x":0, "b":4}
print (list(sorted(diccionario)))

pairs = [[1,2],[-2,3],[4,4],[2,2],[-1,-1]]
print (list(sorted(pairs))) #ordena por el primero parece

pairs = [[1,2],[-2,3],[4,4],[2,2],[-1,-1]]
print (list(sorted(pairs, key=sum))) #ordena por la suma