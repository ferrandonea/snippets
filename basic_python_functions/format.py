txt = "For only {price:.2f} dollars!"
print (txt.format(price=49))

binary_value = format(100,'b')
print (binary_value)

txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)

print (txt1)
print (txt2)
print (txt3)

#Use "<" to left-align the value:

txt = "We have {:<8} chickens."
print(txt.format(49))

#Use ">" to right-align the value:

txt = "We have {:>8} chickens."
print(txt.format(49))
#Use "^" to center-align the value:

txt = "We have {:^8} chickens."
print(txt.format(49))

#Use "=" to place the plus/minus sign at the left most position:

txt = "The temperature is {:=8} degrees celsius."

print(txt.format(-5))

#Use "+" to always indicate if the number is positive or negative:

txt = "The temperature is between {:+} and {:+} degrees celsius."

print(txt.format(-3, 7))

#Use "-" to always indicate if the number is negative (positive numbers are displayed without any sign):

txt = "The temperature is between {:-} and {:-} degrees celsius."

print(txt.format(-3, 7))

#Use " " (a space) to insert a space before positive numbers and a minus sign before negative numbers:

txt = "The temperature is between {: } and {: } degrees celsius."

print(txt.format(-3, 7))

#Use "," to add a comma as a thousand separator:

txt = "The universe is {:,} years old."

print(txt.format(13800000000))

#Use "_" to add a underscore character as a thousand separator:

txt = "The universe is {:_} years old."

print(txt.format(13800000000))

#Use "b" to convert the number into binary format:

txt = "The binary version of {0} is {0:b}"

print(txt.format(5))

#Use "d" to convert a number, in this case a binary number, into decimal number format:

txt = "We have {:d} chickens."
print(txt.format(0b101))

#Use "e" to convert a number into scientific number format (with a lower-case e):

txt = "We have {:e} chickens."
print(txt.format(5))

#Use "E" to convert a number into scientific number format (with an upper-case E):

txt = "We have {:E} chickens."
print(txt.format(5))

#Use "o" to convert the number into octal format:

txt = "The octal version of {0} is {0:o}"

print(txt.format(10))

#Use "x" to convert the number into Hex format:

txt = "The Hexadecimal version of {0} is {0:x}"

print(txt.format(255))

#Use "X" to convert the number into upper-case Hex format:

txt = "The Hexadecimal version of {0} is {0:X}"

print(txt.format(255))

#Use "%" to convert the number into a percentage format:

txt = "You scored {:%}"
print(txt.format(0.25))

#Or, without any decimals:

txt = "You scored {:.0%}"
print(txt.format(0.25))





'''
https://www.w3schools.com/python/ref_string_format.asp

'''