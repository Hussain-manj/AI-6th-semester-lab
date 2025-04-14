# Find numbers divisible by 7 and multiple of 5 between 1500 and 2700:

numbers = []
for num in range(1500, 2701):
    if num % 7 == 0 and num % 5 == 0:
        numbers.append(num)
print(numbers)


# Convert temperatures between Celsius and Fahrenheit:

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

print(f"60°C is {celsius_to_fahrenheit(60):.0f}°F")
print(f"45°F is {fahrenheit_to_celsius(45):.0f}°C")


# Guess a number between 1 and 9:

import random

number = random.randint(1, 9)
guess = None

while guess != number:
    guess = int(input("Guess a number between 1 and 9: "))
    if guess < number:
        print("Too low, try again.")
    elif guess > number:
        print("Too high, try again.")
    else:
        print("Well guessed!")


# Construct a pattern using nested for loops:

for i in range(5):
    for j in range(i):
        print("*", end="")
    print()


# Reverse a word:

word = input("Enter a word: ")
reversed_word = word[::-1]
print(f"The reversed word is: {reversed_word}")


# Count even and odd numbers from a series:

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Number of even numbers: {even_count}")
print(f"Number of odd numbers: {odd_count}")


# Print each item and its type from a list:

# data_list = [1452, 11.23, 1+2, True, 'w3resource', (0, -1), [5, 12], ['dass"?V', "section"?A'H"]]

for item in data_list:
    print(f"{item}: {type(item)}")


# Print numbers from 0 to 6 except 3 and 6:

for num in range(7):
    if num == 3 or num == 6:
        continue
    print(num, end="")


# Get the Fibonacci series between 0 and 50:

a, b = 0, 1
fibonacci = [a, b]

while b <= 50:
    a, b = b, a + b
    fibonacci.append(b)

print(", ".join(map(str, fibonacci)))


# Generate a 2D array based on input rows and columns:

m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))

array = [[i + j for j in range(n)] for i in range(m)]
print(array)


# Accept a sequence of lines and print them in lowercase:

lines = []
while True:
    line = input()
    if not line:
        break
    lines.append(line.lower())

print("\n".join(lines))


# Print binary numbers divisible by 5:

binary_numbers = input("Enter comma-separated binary numbers: ").split(",")
divisible_by_5 = []

for binary_num in binary_numbers:
    if int(binary_num, 2) % 5 == 0:
        divisible_by_5.append(binary_num)

print(",".join(divisible_by_5))


# Calculate the number of digits and letters in a string:

data = input("Enter a string: ")
letters = 0
digits = 0

for char in data:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1

print(f"Letters: {letters}")
print(f"Digits: {digits}")


# Validate password input by users:

import re

def validate_password(password):
    if len(password) < 6 or len(password) > 16:
        return False
    if not any(char.isalpha() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char in ["$", "@"] for char in password):
        return False
    return True

password = input("Enter a password: ")
if validate_password(password):
    print("Valid password")
else:
    print("Invalid password")
