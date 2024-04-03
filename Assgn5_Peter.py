#File: Assgn5_Peter.py
#Project: CSIS2101 Assignment 5
#Author: Peter Cruz
#History: Version 1.1 February 12, 2023

def main():
    print()

    def Peter_fav_sport():
        sp = input("Please enter your favorite sport: ")
        print("My favorite sport is", sp)
    
    Peter_fav_sport()

    print()
    
    n = int(input("Please enter the number of rows you would like to be printed: "))
    def Peter_nested_loop(n):
        for i in range(n+1, 0, -1):
            print()
            for j in range(1, i):
        
                print(j, end = " ")

    Peter_nested_loop(n)

    print()

    def Peter_nursery_rhyme(name, power):
        print("Old MacMarvel had a universe, E-I-E-I-O")
        print("And on his universe he had a", name, "E-I-E-I-O")
        print("With a", power, "here and a", power, "there")
        print("Everywhere a", power)
        print("Old MacMarvel had a universe, E-I-E-I-O")

    Peter_nursery_rhyme("Cyclops", "Heat-Vision")
    Peter_nursery_rhyme("Iron Man", "Repulsor Blast")
    Peter_nursery_rhyme("Hulk", "Hulk Smash")
    

    print()

main()
