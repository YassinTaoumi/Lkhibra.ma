# implicit type conversion 

num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("datatype of num_int:",type(num_int))
print("datatype of num_flo:",type(num_flo))

print("Value of num_new:",num_new)
print("datatype of num_new:",type(num_new))


num_int = 123
num_str = "456"

print("Data type of num_int:",type(num_int))
print("Data type of num_str:",type(num_str))

print(num_int + num_str) # will cause an error because we can't concatenate string with integer

# Explicit type conversion 
# the form : <required_datatype>(expression)

num_int = 123
num_str = "456"
num_flo = 123.5

print(type(num_int))
print(type(num_str))

# Type Casting str to int 
num_str = int(num_str)
print("Data type of num_str after Type Casting:",type(num_str))

num_sum = num_int + num_str
print(num_sum)

# print("Sum of num_int and num_str:",num_sum)
# print("Data type of the sum:",type(num_sum))

# num_flo = int(num_flo)
# print(num_flo)