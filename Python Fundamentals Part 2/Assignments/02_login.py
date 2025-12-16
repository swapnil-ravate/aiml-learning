username = input("Enter username: ")
password = input("Enter Password: ")

if (username == "admin" and password == "pass"):
    print("LOGIN Successful!")

elif (username != "admin"):
    print("wrong Username")

else:
    print("Wrong Password")
