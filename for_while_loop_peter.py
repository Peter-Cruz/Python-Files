#File: BasicLoops.py
#Project: CSIS2101 Assignment 4
#Author: Peter Cruz
#History: Version 1.1 February 5, 2023

#The purpose of this program is to create basic count controlled loops

def for_while_loop_peter():

#Loop 1: a while loop that counts down to -13 starting from -3
    for num in range(-3, -13, -1):
        print (num, end=" ")

#To acquire the desired period at the end of the statement put the -13 in a string with a period at the end once the loop reaches -12
        if num == -12:
            print("-13.")

#This is to make the program look cleaner after being ran
    print("\n")

#Loop 2: A for loop that prints out the values from 15 to 50, counting by five, and the value can not be divisible by 3 and 5
    for num in range(15, 50, 5):

#Numbers that are divisible by two numbers can be removed by using the following equation.  If a number is divisible by both its remainder will = 0
        if (num/5)% 3 != 0:
            print(num, end=", ")

#To drop the comma and space after the 50 follow similar steps to the first loop's period
            if num == 40:
                print("50")

    print("\n")

#Loop 3: A loop where the user inputs the integer parameter as "n". A statement will be printed that many times
    num = int(input("Please enter an integer for the level: "))

#the variable level takes the place of the tpyical counter variable
    level = 1

    while level <= num:
        print("I am on level", level, "of the game.")
        level = level + 1 #this is what allows the loop to continue adding levels until the input num is reached.

    print("\n")

#Loop 4: A loop where the user inputs an integer that will count down only by even numbers until 0 is reached.
#If an odd number is input, the program should go to the even number just above the input and then count down.
    number = int(input("Please enter an integer to count down to zero from: "))
    
    for num in range(number, -2, -2):
#Using the % 2 allows the program to recognize if the num is even or odd.  If the equations value = 0 it is even, if not it is odd.
        if (number % 2) == 0:
            print(num, end=" ")
        elif (number % 2) != 0:
            print(num + 1, end=" ")

    print("\n")

#Loop 5: A loop where the user inputs an integer and count all of the numbers from one until
# it reaches the input.
    
    param = int(input("Please input an integer for the loop to count up to: "))

#Simply state that the parameter is the highest number in the range and it will not be included.  If one wanted the parameter to be included, use param + 1 instead.
    for num in range(1, param, 1):
        print(num, end=" ")

for_while_loop_peter()