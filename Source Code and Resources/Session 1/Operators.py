# Arithmetic Operators 
val1 = 2
val2 = 3
  

res = val1 + val2
print(res)


res = val1 - val2
print(res)

res = val1 * val2
print(res)

res = val1 / val2
print(res)

res = val1 // val2 # divides two numbers and rounds the result down to the nearest integer.
print(res)

res = val1 % val2 # It returns the remainder of dividing the left hand operand by right hand operand.
print(res)

res = val1 ** val2 # The ** operator in Python is used to raise the number on the left to the power of the exponent of the right.
print(res)


# Comparison Operators 

a = 5  
b = 6

print(a != b)
print(a == b)
print(a > b)
print(a < b)
print(a >=b )
print(a <= b)

# Python equality operators (==, !=) are used to compare objects based on their values

# Logical Operators 
a = True 
b = False
print(a and b)
print(a or b)

# Idendity Operators 

x1 = 5
y1 = 5
x2 = 'Hello' #  Python identity operators (is, is not) are used to compare objects based on their identity.
             #  the identity of an object refers to its location in memory.  
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

# Output: False
print(x1 is not y1)

# Output: True
print(x2 is y2)

# Output: False
print(x3 is y3)

# Membership Operators 

x = 'Hello world'

print('H' in x)

print('hello' not in x)
