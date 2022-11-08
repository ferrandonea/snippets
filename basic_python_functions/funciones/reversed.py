# reverse an iterable

lst = [1,2,3]
lst_reversed = reversed(lst)
print (lst_reversed) #iterator
print (list(lst_reversed))

tup = (1,2,3)
print (list(reversed(tup)))

string_ = "hola"
print (list(reversed(string_)))
print (reversed(string_))
print ("".join(reversed(string_)))