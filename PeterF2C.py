#File: PeterF2C
#Project: CSIS2101 Assignment 2
#Author: Peter Cruz
#History: Version 1.1 January 22, 2023

def main():
    name = input("Please enter your name: ")

    print("Hello,",name,"! This program will convert any temperature in degrees fahrenheit to celcius for you!")

    peterFahr = float(input("Please enter the temperature in degrees Fahrenheit that you wish to convert: "))

    K = 32

    cruzCels = (peterFahr - K)*(5/9)

    print( f"The temperature: {peterFahr:.2f} in degrees Fahrenheit is equal to the temperature: {cruzCels:.2f} in degrees Celcius.")
    print("Thank you for using this program, I hope it was useful!")

main()
