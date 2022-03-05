x = "Hello World"                           # this is a string(str)
print(type(x))

y = -20000                                  # this is an Integer(int)
print(type(y))
print(y)

z = 20.5                                    # this is a Float
print(type(z))

c = 2 + 1j                                  # this is a complex
print(type(c))

b = True                                    # this is a boolean(bool)
print(type(b))

L = ["apple", "banana", "cherry"]             # this is a list
print(type(L))

T = ("apple", "banana", "cherry")             # this is a tuple(ordered and unchangeable)
print(type(T))

R = range(6)                                   # this is a range
print(type(R))

D = {"name" : "John", "age" : 36}              # this is a dictionary(dict)
print(type(D))

S = {"apple", "banana", "cherry"}               # this is a set(unordered,unchangeable,and unindexed)
print(type(S))
print(x)

#Variables in Python 

# Creating a variable
x = 5
y = "John"

# Variables Names 
myvar = "Ahmed"
my_var = "Ahmed"
_my_var = "Ahmed"
myVar = "Ahmed"
MYVAR = "Ahmed"
myvar2 = "Ahmed"

# don't do 

2myvar = "Ahmed" # incorrect because we start the name with a number
my-var = "Ahmed" # incorrect because we use a dash in the name
my var = "Ahmed" # incorrect because we leave a space inside the variable's name

# Good to know 

# Camel case : Second and subsequent words are capitalized
#to make word boundaries easier to see.ex: numberOfCollegeGraduates

# Pascal case : Identical to Camel Case, except the first word is also capitalized
# ex: NumberOfCollegeGraduates

# Snake Case: Words are separated by underscores. ex: number_of_college_graduate

# variables names are case sensitive
a = 5
A = 6
print(a)
print(A)

# Many values to multiple variables

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One value to multiple Variables 
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a list 
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Specifying the type of a variable
x = str(3)    # x will be '3'

y = int(3.25)    # y will be 3

z = float(3)  # z will be 3.0