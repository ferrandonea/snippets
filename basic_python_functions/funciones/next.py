class Iterator:
    def __init__(self, start, stop):
         self.start = start
         self.stop = stop
    def __iter__(self):
        self.cur = self.start
        return self
    def __next__(self):
        if self.cur >=self.stop:
            raise StopIteration
        
        self.cur +=1
        return self.cur -1
    
custom_obj = Iterator(1,10)
obj_iter = iter(custom_obj)
print (next(obj_iter))
print (next(obj_iter))
print (next(obj_iter))

lst = ["a", "b", "c"]
lst_iter = iter(lst)
print (next(lst_iter))
print (next(lst_iter))
print (next(lst_iter))

print (next(lst))    