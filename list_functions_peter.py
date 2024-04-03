#File: list_functions_peter
#Project: CSIS2101 Assignment 8
#Author: Peter Cruz
#History: Version 1.1 March 19, 2023

import random #This is for the second, randomly generated list.
def peter_list():
    number_list = [] #Create an empty list so the items can be properly added in the next steps
    n = int(input("Enter the number of items to add to the list: ")) #To properly create a list of numbers, the program needs to know how long the list is.

    for i in range(n):
        item = input("Enter item {}: ".format(i+1)) 
        number_list.append(int(item)) #This appends the entered items into number_list


    number_list_copy = []
    for i in number_list:
        number_list_copy.append(i) #Similar to the original list, this takes the values in the original and appends them to the copy.
    number_list_copy.sort() #This is how the list 1 copy is sorted in order.

    number_list2 = random.sample(range(10,39), len(number_list)) #random.sample(range()) takes the values entered in the range like 10,39 to be selected from.
    #It also selects the same amount of values as number_list using len(number_list) in the length of the list.

    list_range = range_of_list_peter(number_list) #This is where all of the functions are called.  They are set equal to variables to make printing them easier later.
    list_mean = mean_of_list_peter(number_list)
    list_median = median_of_list_peter(number_list_copy)
    list_minus = minus_lists(number_list, number_list2)
    list_plus = plus_lists(number_list, number_list2)

    print()
    print(f"Given list: {number_list}")
    print(f"Range of the List is: {list_range}")
    print(f"Mean of the List is: {list_mean}")
    print(f"Median of the List is: {list_median}")
    print()
    print(f"Second list created using random numbers is: {number_list2}")
    print(f"Plus of the Lists is: {list_plus}")
    print(f"Minus of the Lists is: {list_minus}")
    print()
    #These print statements are what the user will read once the program has finished running.  I use empty prints to format the statements.

def range_of_list_peter(number_list):
    range = (max(number_list), min(number_list)) #Finding the range is as simple as printing the max and min values of the list.
    return range #All of the returns in these functions are placed into where they are called in peter_list.

def mean_of_list_peter(number_list):
    mean = sum(number_list) / len(number_list) #The mean is just the sum of the values of the list divided by the length of the list.
    return mean

def median_of_list_peter(number_list_copy):
    listlen = len(number_list_copy)
    if listlen % 2 == 0: #This if/else statement is to determine if the length of the list is even or odd because that can drastically change the value of the mean.
       median = (number_list_copy[listlen//2 - 1] + number_list_copy[listlen//2]) / 2 #Finding the median of an even numbered list is a bit more difficult than an odd list.
       #But this median is equal to the sum of the middle two numbers divided by 2 since the listlen//2 would result in a whole number which is not possible with an even length.
    else: 
       median = number_list_copy[listlen//2] #With an odd length you are able to simply do listlen//2 since the median will just be the middle index in the list.
    return median

def minus_lists(number_list, number_list2):
    minus = [num for num in number_list if num not in number_list2] #This determines the values in that are only in number_list.  If they are also in number_list2 they are not considered.
    return minus

def plus_lists(number_list, number_list2):
    number_list2_copy = []
    for i in number_list2:
        number_list2_copy.append(i) #I created a copy of list 2 similar to list 1 so the changes made by removing the mutual numbers did not affect the orginal list2.

    for num in number_list: #This for loop takes all of the values in list 1...
        if num in number_list2_copy: #...And if those values from list 1 are in list 2 copy which is the same as list 2...
            number_list2_copy.remove(num) #...They are removed here.

    plus = [number_list + number_list2_copy] #Now list 1 and updated list 2 copy are added together to determine the 'plus' list.
    return plus

if __name__ == "__main__": #I was not sure if we were required to use this instead of just calling the main function (peter_list() in this case), but I figured I should do it just in case.
    peter_list()