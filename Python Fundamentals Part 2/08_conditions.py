# if  elif  else
'''
age = int(input("Enter the Value : "))

if age >= 18:
    print("You can Vote")
    print("You can Drive")

else:
    print("You can't Vote or Drive")
'''

'''
#traffic light example

color = input("Enter Color : ")

if color == "red":
    print("Stop")

elif color == "green":
    print("Go")

elif color == "yellow":
    print("Look")

else:
    print("Wrong color for Traffic Lights")
'''

age = int(input("Enter Age: "))

if (age < 13) :
    print("You are Child.")

elif (age >= 13 and age < 18):
    print("Teeneger.")

elif (age >= 18):
    print("Adult.")
