#!/usr/bin/env python
# coding: utf-8

# # Strings in Python : 

# In[ ]:


# Every String in python is stored as a list of characters 


# ![Strings%20in%20Python.png](attachment:Strings%20in%20Python.png)

# In[2]:


# Accessing Values in Strings
var1 = 'Hello World!'
var2 = "Python Programming"

print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])


# In[18]:


# Getting the length of a string 
myvar = "this is a String"
print(len(myvar))


# In[21]:


# Get the last character of a string
last = myvar[len(myvar)-1]
print(last)
# or
print(myvar[-1])


# In[4]:


# Updating Strings
# don't do that 
myvar = "Hello World"
myvar[:5] = ['h','e','l','l','o']


# In[6]:


# Do that instead 
myvar2 = myvar[:5]
print(myvar2)


# In[7]:


# Strings are lists but don't support the lists methods 
# Strings are Immutable
myvar2.pop()


# In[23]:


# Traversal through a string with a loop
# For loop
for character in myvar:
    print(character,end=" ")


# In[26]:


# While loop
i = 0
while i < len(myvar):
    print(myvar[i])
    i +=1


# In[8]:


# Strings Special characters 
# + operator means concatenation 
myvar = "hello "
myvar2 = "World"
print(myvar + myvar2)


# In[9]:


# * operator means repetition
myvar = "hello "
print(myvar*3)


# In[11]:


# Membership operator
myvar = "hello"
print('H' in myvar)
print('H' not in myvar)


# In[30]:


# Strings comparison 
word = 'banana'
if word == 'banana':
    print('All right, bananas.')


# In[35]:


word = 'melon'
if word < 'banana': # the comparison is case sensitive
    print('Your word, ' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word, ' + word + ', comes after banana.')
else:
    print('All right, bananas.')


# In[38]:


# String Formatting operator 
num = int(3)
print(num+ ' is an integer')


# In[40]:


print('%d is an integer'%(num))


# In[ ]:


# %s - String (or any object with a string representation, like numbers)

# %d - Integers

# %f - Floating point numbers

# %.<number of digits>f - Floating point numbers with a fixed 
# amount of digits to the right of the dot.

# %x/%X - Integers in hex representation (lowercase/uppercase)


# In[43]:


var = 12
print("%d world"%(var))


# In[45]:


# Format method

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))


# In[51]:


txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)
print(txt1)
print(txt2)
print(txt3)


# In[52]:


# Formatting types 
# < > ^ 
txt = "We have {:^8} chickens."
print(txt.format(49))


# In[ ]:


# = 
txt = "The temperature is {:=8} degrees celsius."
print(txt.format(-5))


# In[54]:


txt = "The temperature is between {:-} and {:-} degrees celsius."
print(txt.format(-3, 7))


# In[ ]:


txt = "The universe is {:,} years old."
print(txt.format(13800000000))


# In[ ]:


txt = "The binary version of {0} is {0:b}"
print(txt.format(5))


# # String Methods 

# In[78]:


# lower() | upper()
txt = 'hello world'
print(txt.lower())
print(txt.upper())


# In[55]:


# capitalize()
myvar = "this is python"
print(myvar.capitalize())


# In[57]:


# lower() and casefold()
myvar = "THIS IS PYTHON"
print(myvar.lower())
print(myvar.casefold())


# In[61]:


# Center 
# string.center(length, character), the length of the returned string
txt = 'banana'
print(txt.center(50,'_'))


# In[62]:


# count()
# string.count(value, start, end)
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)


# In[63]:


txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24)
print(x)


# In[64]:


# endsWith() 
# string.endswith(value, start, end)
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)


# In[65]:


# find()
# string.find(value, start, end)
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)


# In[68]:


# isalnum()
txt = "Company12"
x = txt.isalnum()
print(x)


# In[70]:


# isalpha()
txt = "CompanyX"
x = txt.isalpha()
print(x)


# In[75]:


# isdecimal() | isdigit()
txt = "125"
print(txt.isdecimal())
print(txt.isdigit())


# In[79]:


# islower() | isupper()
txt = 'hello world'
print(txt.islower())
txt = txt.upper()
print(txt.isupper())


# In[1]:


# join()
myTuple = ("John", "Peter", "Vicky")

x = " ".join(myTuple)

print(x)


# In[81]:


myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)

print(x)


# In[82]:


# replace()
# string.replace(oldvalue, newvalue, count)
txt = "I like bananas"

x = txt.replace("bananas", "apples")

print(x)


# In[83]:


txt = "one one was a race horse, two two was one too."

x = txt.replace("one", "three", 2)

print(x)


# In[84]:


# split()
# string.split(separator, maxsplit)
txt = "welcome to the jungle"

x = txt.split()
print(x)


# In[85]:


txt = "hello, my name is Peter, I am 26 years old"

x = txt.split(", ")

print(x)


# In[87]:


txt = "apple#banana#cherry#orange"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)

print(x)


# In[88]:


# startswith()
# string.startswith(value, start, end)
txt = "Hello, welcome to my world."

x = txt.startswith("wel", 7, 20)

print(x)


# In[4]:


# strip()
txt = "                        banana                            "
print(txt)
print(txt.strip())


# In[7]:


# rstrip()
txt = "     banana     "
print(txt)
print(txt.rstrip())

txt = "banana,,,,,ssqqqww....."

x = txt.rstrip(",.qsw")

print(x)


# In[90]:


txt = ",,,,,rrttgg.....banana....rrr"

x = txt.strip(",.grt")

print(x)


# In[ ]:




