#

x = b'abcdef'
mem = memoryview(x)
print(mem)
print (mem[1])
print (chr(mem[1]))
print (mem[1:4])
print (bytes(mem[1:4]))