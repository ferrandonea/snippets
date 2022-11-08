#junta listas en tuplas

widths = [4,5,6,7,2,1]
heights = [5,3,1,2,3,1]
zipped = zip(widths, heights)
print (zipped)
print (list(zipped))

string_ = "hello"
values = [1,2,3]
zipped = zip(string_, values)
print (list(zipped))
#si tiene tamaño distinto solo lo que alcanza a juntar