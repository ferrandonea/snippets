from re import S
from tracemalloc import start


lst = [4,5,2,4.3,5,7,9,10,-9]
print(sum(lst))

start_sum = sum(lst, start=5) #suma 5 a sum
print (start_sum)

s = {1,4,5,3,2,1} 
print (sum(s)) # no las repetidas