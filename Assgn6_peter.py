#File: Assgn6_Peter.py
#Project: CSIS2101 Assignment 6
#Author: Peter Cruz
#History: Version 1.1 February 25, 2023

#Begin with importing the random library for the computer before defining the main

#Importing both random and math for the future functions that will require them
import random
import math
def main():
    
    print()
    print("Valid choices are: C for Cat, D for Dog, or R for Rat") #This string prints all of th epossible options for the player to use.
    peter_player = input("Please input a choice for the game: ") #This is where the player will input their choice for the game.


    while peter_player != "C" and peter_player != "D" and peter_player != "R": #Using and statements and != allows gthe program to pick out C,D,R inputs and deny everything else.
        print()
        print("The choice you entered is invalid - Please enter a valid choice.")
        print()
        print("Valid choices are: C for Cat, D for Dog, or R for Rat")
        peter_player = input("Please input a choice for the game: ")
        if peter_player == "C" or peter_player == "D" or peter_player == "R": 
            break #The break function allows the while statement to break when one of the correct inputs is used after an incorrect one.
        
    
    peter_comp = random.randrange(5,16,5) #The possible values for C,D,R equal 5,10,15 respectively.  The range that the computer chooses from is these three numbers.
    #This is also where the random library is used since we imported it in the beginning.

    if peter_comp == 5:
        peter_comp = "C"

    elif peter_comp == 10:
        peter_comp = "D"

    else:
        peter_comp = "R"  #This else statement could have also been an elif statement where peter_comp == 15, but it isn't necessary since there is no other possible value past C,D,R.

    print()

    cdr_peter(peter_player, peter_comp)  #This is where the function is called that displays the results of the game.

    print()

    area_of_triangle_peter() #This is where the program calls the next function to be completed.  All of inputs are taken care of in the function itself instead of taking parameters.


def cdr_peter(usr, cmp):  #cdr_peter takes the values that are placed into it from the main and based on that declares the winner of the game after stating the player and computer choices.

    if usr == "C" and cmp == "C":
        print("Player chose Cat")
        print()
        print("Computer chose Cat")
        print()
        print("The game is a tie.")
    elif usr == "C" and cmp == "D":
        print("Player chose Cat")
        print()
        print("Computer chose Dog")
        print()
        print("Computer wins! - The cat is terrified of the dog")
    elif usr == "C" and cmp == "R":
        print("Player chose Cat")
        print()
        print("Computer chose Rat")
        print()
        print("Player wins! - The cat eats the rat")
    elif usr == "D" and cmp == "C":
        print("Player chose Dog")
        print()
        print("Computer chose Cat")
        print()
        print("Player wins! - The cat is terrified of the dog")
    elif usr == "D" and cmp == "D":
        print("Player chose Dog")
        print()
        print("Computer chose Dog")
        print()
        print("The game is a tie.")
    elif usr == "D" and cmp == "R":
        print("Player chose Dog")
        print()
        print("Computer chose Rat")
        print()
        print("Computer wins! - The rat irritates the dog")
    elif usr == "R" and cmp == "C":
        print("Player chose Rat")
        print()
        print("Computer chose Cat")
        print()
        print("Computer wins! - The cat eats the rat")
    elif usr == "R" and cmp == "D":
        print("Player chose Rat")
        print()
        print("Computer chose Dog")
        print()
        print("Player wins! - The rat irritates the dog")
    elif usr == "R" and cmp == "R":
        print("Player chose Rat")
        print()
        print("Computer chose Rat")
        print()
        print("The game is a tie.")

        
def area_of_triangle_peter():
    
    a,b,c = eval(input("Please enter the three sides of a triangle separated by commas: "))  #This is where the functions asks for the values to find the area since it wasn't asked for in the main.

    is_valid_peter(a,b,c) #This next function is called here taking the user's inputs as parameters.

    while is_valid_peter(a,b,c) == False:  #This while loop is to make sure that the user inputs correct values since the function called just before declared them false. 
        print("Invalid input: Sum of any two sides has to be greater than the third side, please try again.")
        print()
        a,b,c = eval(input("Please enter the three sides of a triangle separated by commas: "))
        is_valid_peter(a,b,c) #This calls the testing function again.

    if is_valid_peter(a,b,c) == True:
        area = area_compute_peter(a,b,c) #This calls the function for computing the actual area now that the inputs meet the requirements.

    print(f"Area of a tringale with sides {a}, {b}, and {c} is {area:.2f} sqaure inches.")  #a,b,c are the same variables as earlier, but area is equal to the value returned from the function just called.

def is_valid_peter(a,b,c): #This is where the user's inputs are taken to test that the coorrect conditions are met.  It will return true or false depending on the results.
    if (a+b) > c:
        return True
    else:
        return False

def area_compute_peter(a,b,c): #This function calculates the actual area of the triangle since a,b,c meet all of the proper requirments.
    s = (a+b+c) / 2

    area = math.sqrt(s * (s-a) * (s-b) * (s-c)) #This is where the math library is used since we called it in the beginning

    return area #this area value is returned to where the function is called in is_valid_peter.

main()
