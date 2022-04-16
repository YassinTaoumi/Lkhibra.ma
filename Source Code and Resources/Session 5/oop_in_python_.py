# -*- coding: utf-8 -*-
"""OOP in Python .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KAATnKRAekmoVUHA3cKJEbO0ZN0prnv2
"""

# Create a class in python 
class Dog:
    pass
print("hello world")

# Create the constructor
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Initiate an Object from a class in python 
d1 = Dog("Rocky", 4)
d2 = Dog("Lisa",5)
d3 = Dog("Oscar",2)
print(d1,d2,d3,sep="-")

# it's necessary to pass all the arguments in the constructor
d = Dog()

# Accessing the attributes of an object 
d = Dog("Mickel",3)
print(d.age)

# Delete the Attributes of an object
del d.age
print(d.age)

# Delete an Object 
dog = Dog("Rocky", 4)
del dog 
print(dog.name)

# Change the attributes of an object 
d.name = "John"
print(d.name)

# Modify the arrtibutes of an object through a method 
class Dog:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def change_name(self,new_name):
        self.name = new_name

first_dog = Dog("Nancy",3)
print(first_dog.name)

first_dog.change_name("Lucy")
print(first_dog.name)

# set a default value for an attribute
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.weight = 0

# instance methods 
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

d = Dog("Alfonso",5)
d.description()

d.speak("Hello")

# Change the output of print of an object 
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

d = Dog("Micky",6)
print(d)

# Inheretance 
class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

class ElectricCar(Car):
    
    def __init__(self, make, model, year):    
        #Initialize attributes of the parent class.
        # you can also use 
#         Car.__init__(self,make, model, year)
        super().__init__(make, model, year)
        self.battery_size = 70 # you can also pass it through the parameters of the constructor
    
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

# Defining Attributes and Methods for the Child Class
class ElectricCar(Car):
    
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70
        
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

# Overriding Methods from the Parent Class
def Electriccar(Car):
    
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70
        
    def get_descriptive_name():
        long_name = "this is an electric car "+str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

my_tesla = Electriccar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())









