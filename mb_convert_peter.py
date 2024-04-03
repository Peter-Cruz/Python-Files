#File: mb_convert_peter.py
#Project: CSIS2101 Assignment 7 1/2
#Author: Peter Cruz
#History: Version 1.1 March 12, 2023
    
def conv_byte_peter(mb):
    byte = (mb*1024)*1024 
    return byte

def conv_kb_peter(mb):
    kb = (mb*1024) #A kb is 1/1024 of a mb so to compsensate for that number just multiply the mb value by 1024
    return kb

def conv_gb_peter(mb):
    gb = (mb/1024) #The same process as for a kb except that the mb is 1/1024 of a gb so just show what that very value would be
    return gb

def conv_tb_peter(mb):
    tb = (mb/1024)/1024
    return tb

#These conversions are each called separately in the other file and because of that they each return only their value after they have been called.