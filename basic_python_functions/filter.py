#requiere una filter function
def filter_func(value):
    return value % 2 == 0

lst = [1,2,3,4,5,6,7,8,9,10]
evens = filter(lambda x: x %2 == 0 , lst) #se puede hacer con funcion anónima
evens_2 = filter(filter_func, lst)
print (evens)
print (evens_2) #es un iterator

print (list(evens))
print (list(evens_2))