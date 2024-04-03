#mod_rec_peter.py

import proc_rec_peter

def main():
    item = input('Please enter the name of the item to be updated: ')
    item_price = float(item.split('$')[1]) #Since the user inputs the item we want to make sure that we can find the specific price of it so we can increase it.
    new_price = item_price * 1.10 #This is the equation to increase the price by 10%

    menu = open(r"C:\CSIS 2101\menu.txt", 'r')
    update_menu = open(r"C:\CSIS 2101\update_menu.txt", 'w')

    lines = menu.readlines() #This reads all of the lines in the document.
    item_found = False #Setting the item as not found means that after all of the lines have been read it can be confirmed that it wasn't found in the file.

    for i in range(len(lines)):
        line = lines[i]

        if item in line: 
            item_found = True #This replaces the false value from before to prove that the item was actually found in the file
            new_line = line.replace(str(item_price), str(new_price)) #This variable uses the replace function to change the price to the new one we calculated earlier into a new line.
            update_menu.write(new_line) #Now the menu is updated to include this new line which only changes the price of the item.
        else:
            update_menu.write(line) #This else condition does not replace anything
        
    if item_found == True:
        print('Record has been modified.  You can find the updated menu in the file update_menu.txt.') #A confirmation message to let the user know the price was changed
    else:
        print('Item was not found, so it could not be modified.') #A confirmation message, but it tells the user nothing was changed because the item was not found.

    menu.close()
    update_menu.close()

    avg_price = proc_rec_peter.calc_price_menu_peter(update_menu)
    print(f'The new average price of the menu is: ${avg_price:.2f}')

if __name__ == '__main__':
    main()