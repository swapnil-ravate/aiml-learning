
'''
9. Nested if
------------
An if statement inside another if statement.
'''

username = input("Enter the Username: ")
password = input("Enter the Password: ")

if (username == "admin" and password == "pass"):
    print("LOGIN Successful!")

else:
    if(username != "username"):
        print("Username Incorrect")
                                    # its called Nesting
    else:
        print("Password Incorrect")