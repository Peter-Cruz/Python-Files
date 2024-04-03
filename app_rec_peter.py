#app_rec_peter

import proc_rec_peter

def main():
    menu = open(r"C:\CSIS 2101\menu.txt", 'a') #Using the 'a' means that you are appending an item to a file.

    new_menu = menu.write('Taco $4.99' + '\n') #This wasn't made to be user input so tacos were hardcoded in as asked.  
    #So it is written into a new variable that opens the old menu and just adds the tacos and price

    menu.close()

    avg_price = proc_rec_peter.calc_price_menu_peter(new_menu) #This calls the function from the first program to find the average and return it here.

    print(f'The new average price of the menu is: ${avg_price:.2f}')

if __name__ == '__main__':
    main()