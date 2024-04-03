#File: Assgn9cruz
#Project: CSIS2101 Assignment 9: Strings
#Author: Peter Cruz
#History: Version 1.1 March 26, 2023

def main():
#Q1
    #I thought that informing the user of the functions of the programs before they used them would make sense for a professional program.
    print("This program will return the index of the second instance a substring is found within a string.")
    print("If the substring is not found or there is only one instance, -1 will be returned.")
    string = str(input("Please input the string you wish to search within: "))
    substring = str(input("Please enter the substring you wish to find: "))
    result = pZ_find(string, substring) #The program takes the two input fields as arguments for the function to utilize.

    if result == -1:  #Using if result == -1 allows the program to take the -1 that is returned from the function.
        print("-1 returned, the substring was either not found or only occurs once.")
    else: #The same thing as before can be said about the else, but since -1 is the only thing that should be returned...
        print("The index of the second occurence is:", result) #...If something is false we can accept pretty much any other outcome.

#Q2
    print()
    print("This next program will convert a phone number containing letters into its numerical counterpart.")
    print("You may enter the phone number as the full 10 digits or the last 7 digits.")
    phone_num = str(input("Please enter the phone number you wish to convert: "))
    low_phone = pZ_number_converter(phone_num.lower()) #I found it easier to just convert the inputs in Q2/Q3 to their lower or upper versions in the main.
    print(f"Your phone number after being converted is: {low_phone}.") #It could have been done in the function itself though.

#Q3   
    print()
    print("This final program will convert your entered sentence into pig latin.") 
    print("You may enter your sentence as in any type-case.")
    sentence = str(input("Please enter the sentence you wish to convert: "))
    up_sentence = pZ_pig_latin(sentence.upper()) #The instructions called for the program to convert the input into all upper-case letters.
    print(f"Your sentence converted into pig latin is: {up_sentence}.")


#Q1
def pZ_find(string, substring):

    first_index = -1
    second_index = -1
    
    for i in range(len(string) - len(substring) + 1): #Finding the range of subtracting the length of the substring from the length of the string...
        #...allows the program to recognize when the last possible occurence of the substring could possibly occur.  
        #Adding 1 to that ensures that the range includes the last possible index.
        if string[i:i+len(substring)] == substring: #This checks to see if the substring can be found and what it's index is.
            if first_index == -1: #If the substring is found then this checks if 'first_index' still = -1, if it does then this index is considered the first index....
                first_index = i #Changing the value of 'first_index' to the value of the current index rather than -1
            elif second_index == -1: #If the substring is found again then it checks if 'first_index' is still = -1 , if it not then it takes this index value...
                second_index = i #...And sets it as the index of 'second_index'
                break #this breaks the for loop since we only needed to find the second index value and since that has been completed we can end the loop.
    
    if second_index == -1: #This if else statement checks to see if 'second_index' is still = -1, if it is then the second index was never found in the string.
        return -1 #Thus, -1 is returned
    else: #In the case that the index is any other value than -1, that value will be returned.
        return second_index

#Q2:
def pZ_number_converter(phone_num):

    numeric_num = '' #Using a new string for the numeric version of the number, this string is where all of the new values will be appended to.
    #The for loop below is where the characters are converted into their numeric counterpart through the if/else statement.
    for char in phone_num:
        if char in ['a', 'b', 'd']:
            numeric_num += '2' #For every subsequent elif, just like this if, this is where the num value is appended to the list based on the alphabet character.
        elif char in ['c', 'e', 'f']:
            numeric_num += '3'
        elif char in ['g', 'g', 'j']:
            numeric_num += '4'
        elif char in ['i', 'k', 'l']:
            numeric_num += '5'
        elif char in ['m', 'n', 'p']:
            numeric_num += '6'
        elif char in ['o', 'q', 'r', 's']:
            numeric_num += '7'
        elif char in ['t', 'u', 'w']:
            numeric_num += '8'
        elif char in ['v', 'x', 'y', 'z']:
            numeric_num += '9'
        else:
            numeric_num += char #This else part of the statement takes the remaining possible characters that are input and returns them as is.
            #This applies to numbers and other special characters or spaces.

    return numeric_num #The new string will now be returned to where it was called.
 
#Q3:
def pZ_pig_latin(sentence):

    words = sentence.split() #the 'words' variable is a split version of the input sentence based on spaces.

    pl_words = [] #this creates a new empty list for all of the split up words to be appended to later.
    for word in words: #this for loop searches through the new split up 'words' version of 'sentence'.
        pl_word = word[-2:] + word[:-2] + "23" #this takes the last two characters of the 'word' first and then adds the first two characters of that same 'word' behind them.
                                               #'23' is also added as a string to the end of the new 'word'
        pl_words.append(pl_word) #the new versions of the 'word's are appended to the 'pl_words' list.

    pl_sentence = " ".join(pl_words) #.join combines the split 'pl_words' back into the way it was in the original input.

    return pl_sentence #this recombined converted version of the input is now returned in the place where it was called in the main.

    
if __name__ == "__main__":
    main()
