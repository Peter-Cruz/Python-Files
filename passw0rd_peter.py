#passw0rd_peter

import passwd #Import the passwd file so we can use one of its functions later.

def main():
    in_file = open("C:\CSIS 2101\passwdin.txt", 'r') #I was unable to open up the specific file based on just its name, so I used its directory.
    good_psswd_out = open('peter_good_psswd_out.txt', 'w') #This is the good password file 
    bad_psswd_out = open('peter_bad_passwd_out.txt', 'w') #This is the bad password file
    
    line = in_file.readline()

    while line != "":
        line = in_file.readline().rstrip('\n') #This while loop goes through every line in the opened file using each new line as the identifier.
       
        result = passwd.check_password_peter(line) #This is where the passwd file is used to check all of the passwords.

        if result == 'Password Accepted.':
            good_psswd_out.write(line + ': ' + result + '\n') #The passwd file returns a specific message so by checking the valid message we can deny everything else.
        else:                                                 #Both conditions also write the password, the result, and then go to a new line.
            bad_psswd_out.write(line + ': ' + result + '\n')  #Both conditions write specifically to the good or bad files depending on if they meet the conditions.

    in_file.close()
    good_psswd_out.close() #It is important to close out of all of the files that were opened.
    bad_psswd_out.close()

if __name__ == '__main__':
    main()