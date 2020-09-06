

#!/usr/bin/python3
#importing Getpass to block out password
from getpass import getpass

loginDict = {
"test" : "password",
"admin" : "admin",
"root" : "root"
}

# create bolean sting to accept
login = False
# track log in attempts
A = 0 

# while loop to check is login credentials are valid
while login == False:
# Get credentials from users
    name = input("User name:  ")
# getpass will hide password
    value = getpass("password:  ")   
# login credentials are valid
    if name in loginDict:
       if value == loginDict[name]:
           login = True
           break
# give user 5 attempts if they fail
       else: 
           print("Try Again!")
           A += 1
           
    else:
        print("Try Again!")     
        A += 1
        
    if (A >= 5):
        break
# after 5 attempts they can't try anymore
if (A >= 5):
     print("Authorized Personnel Only")
# They successfully logged in
else:
    print("Logging in")
