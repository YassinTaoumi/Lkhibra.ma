#!/usr/bin/env python
# coding: utf-8

# # Data Structures in Python : 

# ## Lists : 

# In[ ]:


# Lists : 
# Lists are used to store multiple items in a single variable.

# Create a List:
thislist = ["apple", "banana", "cherry"]
print(thislist)


# In[3]:


# Create a blank List 
thislist_2 = []
thislist_2
thislist = list()
print(thislist)


# In[ ]:


# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.

# Lists allow duplicates : 
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)


# In[ ]:


# list length : 
thislist = ["apple", "banana", "cherry"]
print(len(thislist))


# In[ ]:


# list items datatype 
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]


# In[2]:


# A list can contain different data types:
list1 = ["abc", 34, True, 40, "male"]
print(list1)


# In[ ]:


# Access List Items : 
thislist = ["apple", "banana", "cherry"]
print(thislist[1])


# In[3]:


# Negative Indexing
thislist = [1, 5, 7, 9, 3]
print(thislist[-1])


# In[ ]:


# Range of Indexes

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# The search will start at index 2 (included) and end at index 5 (not included).
print(thislist[2:5])


# In[ ]:


# By leaving out the start value, the range will start at the first item:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])


# In[ ]:


# By leaving out the end value, the range will go on to the end of the list:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])


# In[ ]:


# Range of Negative Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])


# In[ ]:


# Check if Item Exists 
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


# In[ ]:


print(thislist.index("banana"))


# In[ ]:


# Change Item Value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


# In[ ]:


# Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


# In[5]:


# If you insert more items than you replace, the new items will be inserted 
# where you specified
#and the remaining items will move accordingly
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)


# In[6]:


thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)


# In[ ]:


# Insert Items
thislist = ["apple", "banana", "cherry"]
# insert method form : insert(position , value )
thislist.insert(2, "watermelon")
print(thislist)


# In[ ]:


# Append Items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange") # the append method adds the element in the end of the list 
print(thislist)


# In[ ]:


# Extend List
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


# In[7]:


thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange") # this is a tuple 
thislist.extend(thistuple)
print(thislist)


# In[37]:


# Remove Specified Item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


# In[ ]:


# Remove Specified Index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)


# In[ ]:


thislist = ["apple", "banana", "cherry"]
thislist.pop() # without index pop removes the last element 
print(thislist)


# In[ ]:


thislist = ["apple", "banana", "cherry"]
del thislist[0] # del also for deleting a specified index element 
print(thislist)


# In[8]:


# Delete a list completely 
thislist = ["apple", "banana", "cherry"]
del thislist
thislist


# In[9]:


# Clear the List
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


# In[ ]:


# Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x) 


# In[ ]:


thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


# In[ ]:


# Sort List Alphanumerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


# In[ ]:


thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)


# In[ ]:


# Sort Descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)


# In[12]:


thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)


# In[13]:


# Case Insensitive Sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)


# In[14]:


# Reverse Order
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


# In[15]:


# Copy a List
# don't do That 
thislist = ["apple", "banana", "cherry"]
mylist = thislist
# thislist.pop()
# print(thislist)
# print(mylist)


# In[16]:


# Instead do that 
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
# thislist.pop()
# print(thislist)
# print(mylist)


# In[ ]:


# Another way to make a copy of a list 
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)


# In[17]:


# Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


# In[ ]:


# Using Extend 
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)


# <!-- 
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list 
# -->

# ## Tuples :

# In[ ]:


# A tuple is a collection which is ordered and unchangeable. 
# Create a Tuple 
thistuple = ("apple", "banana", "cherry")
print(thistuple)


# In[4]:


# Create blank tuple
thistuple = tuple()
thistuple


# In[ ]:


# Allow Duplicates 
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)


# In[ ]:


# Tuple Length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))


# In[ ]:


# Create Tuple With One Item
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))


# In[ ]:


# Tuple Items
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)


# In[ ]:


tuple1 = ("abc", 34, True, 40, "male")


# In[ ]:


# Access Tuple Items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])


# In[ ]:


# Negative Indexing
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])


# In[ ]:


# Range of Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])   #[:4] | [2:]


# In[ ]:


# Range of Negative Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])


# In[21]:


# Check if Item Exists
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")


# In[23]:


# Another way 
thistuple.index("aple")


# In[ ]:


# Change Tuple Values
x = ("apple", "banana", "cherry") 
y = list(x)
y[1] = "kiwi" # Convert the tuple into a list to be able to change it
x = tuple(y)

print(x)


# In[24]:


# Unpacking a Tuple
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits
# green , yellow , red = fruits 

print(green)
print(yellow)
print(red)


# In[26]:


# Using Asterisk
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)


# In[ ]:


# Loop into a tuple 
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)


# In[ ]:


# Join Two Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


# In[ ]:


# Multiply Tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)


# In[27]:


# Count 
MyTuple = ("Oumaima","Mehdi","Youness","Oumnia","Mehdi")
print(MyTuple.count("Mehdi"))


# In[ ]:


# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position 
# of where it was found


# ## Sets : 

# In[30]:


# A set is a collection which is unordered, unchangeable*, and unindexed.
# Creating a set 
myset = {"apple", "banana", "cherry"}
print(myset)


# In[ ]:


# Duplicates Not Allowed
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)


# In[ ]:


# Get the Length of a Set
thisset = {"apple", "banana", "cherry"}

print(len(thisset))


# In[ ]:


# Set Items
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {"abc", 34, True, 40, "male"}


# In[31]:


# Access Items
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


# In[ ]:


# Check if an item exists in the Set 
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)


# In[ ]:


# Add Items 
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)


# In[ ]:


# Add Sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)


# In[ ]:


thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"] # you can also add lists 

thisset.update(mylist)

print(thisset)


# In[32]:


# Remove Item
thisset = {"apple", "banana", "cherry"}

thisset.remove("apple") # if an item doesn't exist

print(thisset)


# In[34]:


thisset = {"apple", "banana", "cherry"}

thisset.discard("apple")

print(thisset)


# In[ ]:


# Remove the last item 
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)


# In[ ]:


# Clear a set 
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)


# In[38]:


# delete a set 
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)


# In[ ]:


# Join Two Sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)


# In[ ]:


set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)


# In[39]:


# Keep ONLY the Duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)


# In[40]:


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)


# In[ ]:


# add()	Adds an element to the set
# clear()	Removes all the elements from the set
# copy()	Returns a copy of the set
# difference()	Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another
# specified set
# discard()	Remove the specified item
# intersection()	Returns a set, that is the intersection of two other sets
# intersection_update()	Removes the items in this set that are not present in other 
# specified set(s)
# isdisjoint()	Returns whether two sets have a intersection or not
# issubset()	Returns whether another set contains this set or not
# issuperset()	Returns whether this set contains another set or not
# pop()	Removes an element from the set
# remove()	Removes the specified element
# symmetric_difference()	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	Return a set containing the union of sets
# update()	Update the set with the union of this set and others


# ## Dictionary :

# In[42]:


# Key : value
# Creating a dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


# In[43]:


# Duplicates Not Allowed
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)


# In[44]:


# Dictionary Length
print(len(thisdict))


# In[45]:


# Dictionary Items
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)


# In[54]:


# Accessing Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)


# In[48]:


# Another way 
x = thisdict.get("model") # we search with the key not the value 
print(x)


# In[49]:


# Get Keys
x = thisdict.keys()
print(x)


# In[52]:


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change


# In[57]:


# Get Values
x = thisdict.values()
print(x)


# In[ ]:


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change


# In[58]:


# Get Items
x = thisdict.items()
print(x)


# In[ ]:


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change


# In[ ]:


# Check if Key Exists
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")


# In[ ]:


# Change Values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018


# In[ ]:


# Update Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})


# In[ ]:


# Adding Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)


# In[ ]:


# Update Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})


# In[ ]:


# Removing Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)


# In[ ]:


# Another way 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem() #remove the last item 
print(thisdict)


# In[ ]:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)


# In[ ]:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.


# In[ ]:


# Clear a dict 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)


# In[61]:


# Copy a Dictionary
# Don't do that 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict
mydict.pop("year")
print(mydict)
print(thisdict)


# In[ ]:


# Do instead 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)


# In[ ]:


# Nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}


# In[ ]:



child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}


# In[62]:


# from keys 
x = ('key1', 'key2', 'key3')

thisdict = dict.fromkeys(x)

print(thisdict)


# In[ ]:


# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist
# insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




