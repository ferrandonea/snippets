lst = [1,1,2,2,1,2,2,3,3,4,2,1,3]
print (set(lst))

s = {6,6,7,*lst} #unpacking
print (s)

new_set = set()
print (type(new_set))

new_dict = {}
print (type(new_dict))