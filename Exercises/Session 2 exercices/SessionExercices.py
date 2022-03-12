"""
Reverse a list in Python
"""

"""
Concatenate two lists index-wise 
example : 
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
=> ['My', 'name', 'is', 'Kelly']
"""

"""
Turn every item of a list into its square:
numbers = [1, 2, 3, 4, 5, 6, 7]
=> [1, 4, 9, 16, 25, 36, 49]
"""


"""
Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
=> ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
"""


"""
Remove empty strings from the list of strings
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
=> ["Mike", "Emma", "Kelly", "Brad"]
"""

"""
Convert two lists into a dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
=> {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
"""

"""
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
Print the value of key ‘history’ from the below dict
"""

"""
Initialize dictionary with default values
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
=> {'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}
"""

"""
Delete a list of keys from a dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]
=> Expected output : {'city': 'New york', 'age': 25}
"""

"""
Check if a value exists in a dictionary
sample_dict = {'a': 100, 'b': 200, 'c': 300}
=> output : 200 present in a dict
"""

"""
Rename key of a dictionary 
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
=> output : {'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}
"""

"""
Change value of a key in a nested dictionary
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
=> output ; {
   'emp1': {'name': 'Jhon', 'salary': 7500},
   'emp2': {'name': 'Emma', 'salary': 8000},
   'emp3': {'name': 'Brad', 'salary': 8500}
}
"""

"""
Reverse the tuple
tuple1 = (10, 20, 30, 40, 50)
output : (50, 40, 30, 20, 10)
"""

"""
Access value 20 from the tuple
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
output : 20
"""

"""
Check if all items in the tuple are the same 
input : tuple1 = (45, 45, 45, 45)
output : True
"""

"""
 Add a list of elements to a set
input : 
sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]
output : 
{'Green', 'Yellow', 'Black', 'Orange', 'Red', 'Blue'}
"""

"""
Check if two sets have any elements in common. If yes, display the common elements
input : 
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
output: 
Two sets have items in common
{10}
"""