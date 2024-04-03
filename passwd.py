#passwd.py
'''
A given string is eligible to be a password
if it contains one lower case character at least one upper case character
at least one digit
no special characters and no spaces.
Also length of the string has to be greater than or equal to 8 characters.
If all these conditions are met string can be a password otherwise tell the user
why it cannot be a password.
'''


def main():
     pswd = input( "Please enter a candidate string: " )

     valid, mesg = check_password_peter( pswd )

     if valid == True:
          print( mesg )
     else:
          print( mesg ) 


def check_password_peter( pswd ):
     lng = len( pswd )
     count_uc = 0
     count_lc = 0
     count_dig = 0
     count_sc = 0
     count_sp = 0

     for ch in pswd:
          if ch.isupper():
               count_uc += 1
          elif ch.islower():
               count_lc += 1
          elif ch.isdigit():
               count_dig += 1
          elif ch.isspace():
               count_sp += 1
          else:
               count_sc += 1


     if lng >= 9 and count_uc == 3 and count_lc == 3 and count_dig == 1 and count_sp == 0 and count_sc >= 1:
          msg = "Password Accepted."
          return msg
     else:
          msg = "Password not accepted  \n"
          if lng < 8:
               msg += "Password must be at least 9 characters in length. \n"
          if count_lc == 0:
               msg += "Password must contain at least 3 lower case character. \n"
          if count_uc == 0:
               msg += "Password must contain at least 3 upper case character. \n"
          if count_dig == 0:
               msg += "Password must contain only 1 digit. \n"
          if count_sc != 0:
               msg += "Password must contain at least 1 special character. \n"
          if count_sp != 0:
               msg += "Password cannot contain any spaces. \n"

          return msg












          
