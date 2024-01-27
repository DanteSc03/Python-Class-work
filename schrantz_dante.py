# -*- coding: utf-8 -*-
"""Schrantz_Dante.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fpyzTIMjsNDusoNbFrvNi1QcCsZqQms7

# Exercises

1. Create a variable and store a message in it. Print the variable. Rewrite the variable with another message and print it again.
"""

message= "Hello There"
print(message)
message= "Hello there fellas"
print(message)

"""2. Save your name in a variable. Using that variable, print your name in lower and upper case letters."""

first= "Dante"
print(first.upper())
print(first.lower())
print(first.title())

"""3. Save your name and surnames in different variables and concatenate them to print your whole name."""

first= "Dante"
last = "Schrantz"
print(first,last)

"""4. Save your name in a variable with blank spaces at both ends. Print it. Remove blank spaces on the left, on the right side and on both sides. Print all the messages."""

first=" Dante "
print(first)
print(first.strip())

""" 5. Create some commands in Python to check if a number is even or odd and print the result."""

num = 9
if num % 2 == 0:
  print("Even Number")
else:
  print("Odd Number")

num = 8
if num % 2 == 0:
  print("Even Number")
else:
  print("Odd Number")

num = 4285923457
if num % 2 == 0:
  print("Even Number")
else:
  print("Odd Number")

"""6. Create some commands in Python to check if two strings are equal and print the result."""

str1= "apple"
str2= "French Toast"

if str1==str2:
  print("The Strings are the same")
else:
  print("The strings are not the same")

str1= "apple"
str2= "apple"

if str1==str2:
  print("The Strings are the same")
else:
  print("The strings are not the same")

"""7. Imagine you bougth 900 shares of an important Energy company, for a total price 0f 5000 euros 3 years ago. Today you decide to sell them for a price of 5575 euros. Write a program in python that calculates the annual interest rate earned with the benefit of the operation. Define the variables you need and print the information in a clear way."""

import numpy as np
numShares = 900
purchase = 5000
time = 3
selling = 5575

print(selling/purchase)

interest = np.cbrt(selling/purchase)-1

print(interest)

"""8. The Faculty of Economics of the University of Navarra is carrying out a study about the incoming students in the different degrees. In Data Analytics there are 30 students and the 10% are incoming students; in International Economics and finance there are 20 students and 20% are incoming students; in General Management there are 40 students and the 25% are incoming students. Create a program in python that calculates the average number of incoming students in the Faculty. What is the degree with more incoming students? Use comparison operators to get the answer."""

DA = 30
PerDA = 0.1
IncDA = DA*PerDA
IEF = 20
PerIEF = 0.2
IncIEF = IEF*PerIEF
GM = 40
PerGM = 0.25
IncGM = GM*PerGM

print(IncDA)
print(IncIEF)
print(IncGM)

print(IncDA+IncIEF+IncGM)
print((IncDA+IncIEF+IncGM)/3)

print(IncDA>IncIEF)
print(IncIEF>IncDA)
print(IncIEF>IncGM)
print(IncGM>IncIEF)
print(IncDA>IncIEF)
print(IncIEF>IncDA)

"""9. Identify regular patterns in the following strings and write expressions that starting with shorter strings and using concatenation and repetition of strings, you produce the strings shown. Use the variables you need."""

print('%%%%%./././<-><->')

print('........*****---*****---........*****---*****---')

a = "%"
b = "./"
c = "<->"
print(a*5+b*3+c)

d="."
e= "*"
f="-"
print((8*d+5*e+3*f+5*e+3*f)*2)

"""10. Create two boolean variables, is_raining and is_sunny, and assign them values. Print whether it's a good day based on these variables."""

is_raining= False
is_sunny= True

if ((is_sunny == True) & (is_raining== False)):
  print("It's a beautiful day")
else:
  print("It's an ok day")

is_raining= False
is_sunny= False

if ((is_sunny == True) & (is_raining== False)):
  print("It's a beautiful day")
else:
  print("It's an ok day")

is_raining= True
is_sunny= False

if ((is_sunny == True) & (is_raining== False)):
  print("It's a beautiful day")
else:
  print("It's an ok day")


is_raining= True
is_sunny= True

if ((is_sunny == True) & (is_raining== False)):
  print("It's a beautiful day")
else:
  print("It's an ok day")