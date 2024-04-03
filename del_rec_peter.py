#del_rec_peter

import proc_rec_peter

def main():
    item = input('Please enter the item that you wish to be deleted: ')

    menu = open("C:/CSIS 2101/menu.txt", 'r') 
    update_menu = open('update_menu.txt', 'w') 
    lines = menu.readlines() #This reads all of the lines in the file

    if item.strip() in lines:
        new_lines = [] 
        for line in lines:
            if line.strip() != item:
                new_lines.append(line) #This append function should adding all of the lines that don't contain the item into the new list.  However if it does contain the item then it is removed.
        lines = new_lines
        update_menu.writelines(lines)
        print(f'The item "{item}" has been removed from the menu.')
    else:
        print(f'Sorry, the item "{item}" could not be found in the menu.')

    updated_menu = open("C:/CSIS 2101/update_menu.txt", 'r')
    avg_price = proc_rec_peter.calc_price_menu_peter(updated_menu)

    menu.close()
    update_menu.close()
    updated_menu.close()

    print(f'The new average price of the menu is: ${avg_price:.2f}')

if __name__ == '__main__':
    main()
