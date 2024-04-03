#File: menu_peter.py
#Project: CSIS2101 Assignment 7 2/2
#Author: Peter Cruz
#History: Version 1.1 March 12, 2023

import mb_convert_peter #This is where the other file in this assignmnent is imported to use later in this program
#This is the display menu
def menu_peter():
    print("MegaByte Conversion Menu")
    print("-------------------------------")
    print("1. Convert to Bytes")
    print("2. Convert to KiloBytes (KB)")
    print("3. Convert to GigaBytes (GB)")
    print("4. convert to TerraBytes (TB)")
    print("5. Quit the program")
    print()

def main():
    choice = 0
    while choice >= 0:
        menu_peter()

        choice = int(input("Enter your choice: ")) #The user enters their choice from the menu and this is what activates the rest of the main

        if choice == 1:
            print()
            mb = int(input("Enter the data in MegaBytes:  "))
            byte =  mb_convert_peter.conv_byte_peter(mb) #The mb to byte converter is called from the imported file and does the math from that function
            print(f"{mb} MegaBytes is {byte} Bytes.")
            print()


        elif choice == 2:
            print()
            mb = int(input("Enter the data in MegaBytes:  "))
            kb =  mb_convert_peter.conv_kb_peter(mb) #The mb to kb converter is called 
            print(f"{mb} MegaBytes is {kb:0.6f} KiloBytes.")
            print()
        
        elif choice == 3:
            print()
            mb = int(input("Enter the data in MegaBytes:  "))
            gb =  mb_convert_peter.conv_gb_peter(mb) #The mb to gb converter is called
            print(f"{mb} MegaBytes is {gb:0.6f} GigaBytes.")
            print()

        elif choice == 4:
            print()
            mb = int(input("Enter the data in MegaBytes:  "))
            tb =  mb_convert_peter.conv_tb_peter(mb) #The mb to tb converter is called
            print(f"{mb} MegaBytes is {tb:0.6f} TeraBytes.")
            print()

        elif choice == 5:
            print()
            print("Goodbye!")
            break #This is to end the loop that continues to display the menu in all of the other choice values 
        
        else:
            print("Invalid input, please enter again.") #Any other input not already taken care of by the >0 condition is taken here and told to enter another input

if __name__ == "__main__":
    main()