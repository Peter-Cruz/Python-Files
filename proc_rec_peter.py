#proc_rec_peter.py
#Assignment 11

def main():
    menu = open("C:\CSIS 2101\menu.txt", 'r') #Setting the commands as variables so they are easier to call later in the program.

    avg_price = calc_price_menu_peter(menu)\
    
    menu.close() #It is very important to close your program after you are done accessing it.

    print(f'The average price of the menu is: ${avg_price:.2f}') #The average price is printed only using two decimal points like a normal food price.

def calc_price_menu_peter(menu): #This is the average calculator that will be used for all of the subsequent files for this assignment.
    total_price = 0
    item_count = 0

    line = menu.readline()

    while line != '': #This while statement tells the progrma to continue reading the .txt file while the line has content in it.
        item_price = float(line.split('$')[1].strip()) #This variable splits each item up into two parts and gets the numerical price that comes after the '$'
        total_price += item_price #Each individual item price is added onto the total price variable.
        item_count += 1 #The item count also increases so it knows to count through all of the items.

        line = menu.readline()

        avg_price = total_price / item_count #The average price of the menu is based on this division equation

    return avg_price #This returns the average price back to where it was called in the main.


if __name__ == '__main__':
    main()