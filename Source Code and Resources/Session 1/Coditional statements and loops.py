# Conditional Statements 
# if : 
a = 33
b = 200
if b > a:
  print("b is greater than a")

# elif
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

# else 
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# For Loop 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# Break 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

# Continue 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

# range 
for x in range(6):
  print(x)

# else in the for loop 
for x in range(6):
  print(x)
else:
  print("Finally finished!")

for x in range(6):
  if x == 3: break #  The else block will NOT be executed if the loop is stopped by a break statement.
  print(x)
else:
  print("Finally finished!")

# While loop 
i = 1
while i < 6:
  print(i)
  i += 1

# Break Statement 
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# Continue Statement 
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# the else Statement 
i = 1
while i < 6:
    print(i)
    i += 1
else:
  print("i is no longer less than 6")