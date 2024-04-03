#File: PeterC2F.py
#Project: CSIS2101 Assignment 2 pt.2
#Author: Peter Cruz
#History: Version 1.1 January 22, 2023

def main():
    name = input("Please enter your name: ")

    print("Hello,",name,"! This program will convert any temperature in degrees celsius to fahrenheit for you!")

    peterCels = float(input("Please enter the temperature in degrees Celsius that you wish to convert: "))

    K = 32

    cruzFahr = peterCels*(9/5)+K

    print( f"The temperature: {peterCels:.2f} in degrees Celsius is equal to the temperature: {cruzFahr:.2f} in degrees Fahrenheit.")
    print("Thank you for using this program, I hope it was useful!")

main()
