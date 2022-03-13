"""
Accept a list of 5 float numbers as an input from the user and print them
"""
for i in range(6):
    num = float(input("give me a float number"))
    print(num)

"""
Calculate the sum of all numbers from 1 to a given number
"""
number = int(input("Number: "))
sum = 0
for i in range(1, number + 1):
    sum += i
print(sum)

"""
Write a program to print multiplication table of a given number
"""
n = int(input("Enter a number : "))
for i in range(1, 11, 1):
    product = n * i
    print(product)

"""
Display numbers from -10 to -1 using for loop
"""
for num in range(-10, 0, 1):
    print(num)

"""
print numbers from 0 to 20 
and Use else block to display a message “Done” after successful execution of for loop
"""
for i in range(21):
    print(i)
else:
    print("Done!")


"""
Find the factorial of a given number
"""
num = int(input('Give a number: '))
factorial = 1
if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    # run loop 5 times
    for i in range(1, num + 1):
        # multiply factorial by current number
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)


"""
Calculate the cube of all numbers from 1 to a given number
"""
input_number = int(input('Enter a number : '))
for i in range(1, input_number + 1):
    print("Current Number is :", i, " and the cube is", (i * i * i))

"""
Write a program to print n natural number in descending order using a while loop.
"""
number = int(input("Please Enter a Number: "))
i = number

while ( i >= 1):
    print (i)
    i = i - 1


"""
print the following pattern 
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
"""
print("Number Pattern ")

# Decide the row count. (above pattern contains 5 rows)
row = 5
# start: 1
# stop: row+1 (range never include stop number in result)
# step: 1
# run loop 5 times
for i in range(1, row + 1, 1):
    # Run inner loop i+1 times
    for j in range(1, i + 1):
        print(j, end=' ')
    # empty line after each row
    print("")