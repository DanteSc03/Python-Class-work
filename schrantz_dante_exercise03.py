# -*- coding: utf-8 -*-
"""
# Exercises using while loops, input function and processing csv files

**NOTE: Use the commands that we have seen in class up to now.**

1. Write a program that asks by user input deciaml numbers while the user writes greater numbers than the first introduced.
"""

num1 = float(input("Write a decimal number: "))
num2 = float(input("Write a decimal number larger than the previous number: "))
while num1 <= num2:
  print("That's a good choice: ")
  num2 = float(input("Write a number larger than the previous number: "))
print("Unfortunately your number did not meet the criteria :(")

"""2. Write a program that calculates the factorial of a certain number introduced using input user. The program will have to check if the number introduced is an integer."""

factorial = 1
num = int(input("Give me a non negative non decimal number to give its factorial:"))
if num%2 != 2 and num >= 0:
  for i in range(1,num + 1):
       factorial = factorial * i
  print("The factorial of",num,"is",factorial)
else:
  print("",num, "is not an integer")

"""3. Write a program that reads a sequence of integers ending in 0 and returns the count of even numbers it contains. **Note:** We do not include the final 0. Example:
~~~
Introduce a number: 3
Introduce another number: 6
Introduce another number: 2
Introduce another number: 0
There are 2 even numbers
~~~
"""

count = 0
num = int(input("Introduce a number: "))
while num != 0:
  num = int(input("Introduce another number:"))
  if num%2 == 0:
    count += 1
print(f"There are {count} even numbers")

"""4. Write a program that adds integers as the user enters them via keyboard. The program will stop when the sum exceeds 2000. It should inform the user of the total count of numbers entered, the final sum of the numbers, and the highest and lowest values in the sequence.
Example:
~~~
Introduce a number: 648
Introduce another number: 823
Introduce another number: 203
Introduce another number: 784
4 numbers have been introduced, the sum is 2458 and the highest and lowest values are 823 and 203
~~~

    
"""

nums=[]
total_sum=0
count=1
num = float(input("Introduce a number: "))
total_sum = float(num)
while total_sum <= 2000:
  num = float(input("Introduce another number:"))
  nums.append(num)
  total_sum+=float(num)
  count+=1
print(f"{count-1} numbers have been introduced")
print(f"The total is {total_sum}")
print(f"The minimum number is {min(nums)}")
print(f"The maximum number is {max(nums)}")

"""5. Write a program that reads a sequence of characters that ends in a point ('.'), and tells us how many times the letter 'a' appears without taking care if it is in lower or upper case.
Example:  
~~~
Introduce one character: r
Introduce another character: A
Introduce another character: t
Introduce another character: a
Introduce another character: s
Introduce another character: .
There are 2 'a'
~~~

"""

letter=[]
total_sum=0
count=0
num = input("Introduce one character: ")
if letter == "a" or letter == "A":
  count+=1
while letter != ".":
  letter = input("Introduce another character:")
  if letter == "a" or letter == "A":
    count+=1
print(f"there are {count} 'a' ")

"""6. Write a program that reads a sequence of characters ending in '0' and performs a sum according to the following rules:

- Lowercase letters are worth 1 point.

- Uppercase letters are worth 2 points.

- Digits are worth their own numeric value. (For example, '5' is worth 5).

- Any other character is worth 0.

Example:
~~~
Introduce one character: a
Introduce another character: P
Introduce another character: E
Introduce another character: ,
Introduce another character: 4
Introduce another character: 0
The sum is 9
~~~

"""

alt=[]
total_sum=0

while alt != '0':
  alt = input("Introduce another character:")
  if alt.isupper():
    total_sum += 2
  elif alt.islower():
    total_sum += 1
  elif alt.isdigit():
    total_sum += int(alt)
  else:
    total_sum += 0

print(f"The total is {total_sum}")

"""7. Write a program that reads two integer numbers and admit numbers until one is out of the interval.    
Example:
~~~
Introduce lower value: 3
Introduce upper value: 12
Introduce a number: 6  
Introduce a number: 12  
Introduce a number: 10   
Introduce a number: 23  
The 23 is out of the interval
~~~
"""

low = int(input("Introduce a lower value: "))
upper = int(input("Introduce a upper value: "))
num = int(input("Introduce a number:"))


while low <= num <= upper:
  num = int(input("Introduce a number:"))

print(f"The {num} is out of the interval")

"""8. Using the file 'PPR-2015.csv', write a program that calculates the average price of the houses sold in January (the year is alwyas 2015)."""

from google.colab import drive
drive.mount('/content/drive')

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/drive/MyDrive/Colab\ Notebooks/
!ls

import csv
csv_path = "PPR-2015.csv"
n_rows=5

with open(csv_path,"r") as file:
  reader = csv.reader(file)
  for n, row in enumerate(reader):
    print(row)
    if n==n_rows:
      break

import csv
csv_path = "PPR-2015.csv"
n_rows=5
list_h=[]
l_prices=[]
num_col=4

with open(csv_path, "r") as file:
    reader = csv.reader(file)
    for n, row in enumerate(reader):
        list_h.append(row)

for row in range(1, len(list_h)):
    price=list_h[row][num_col]
    price=price.split('.')
    price=price[0]
    l_prices.append(int(price[1:].replace(',', '')))

av_price= sum(l_prices)/len(l_prices)
print(f"The average price of the houses is {av_price:.2f} euros")

"""9. Using the file 'PPR-2015.csv', write a program that calculates how many different postal codes there are in the file and print them."""

import csv
csv_path = "PPR-2015.csv"
n_rows=5
list_h=[]
num_col=2
postal_codes=0
unique_postal_codes = set()

with open(csv_path, "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        if len(row) > num_col:
            postal_code = row[num_col].strip()
            unique_postal_codes.add(postal_code)

num_unique_postal_codes = len(unique_postal_codes)
print(f"The number of unique postal codes are {num_unique_postal_codes} and are the following {unique_postal_codes}")

"""10. Using the file 'PPR-2015.csv', write a program that calculates the average price of the houses sold in the different postal codes and print them both."""

