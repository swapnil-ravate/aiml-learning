# alternate for if...elif...else
# Eska jyada use nahi karte jyada tr code condition ke liye if...else hi use karte hai. 

color = input("Enter Color: ")

match color:
    case "Green":
        print("Go")
    case "Red":
        print("Stop")
    case "Yellow":
        print("Look")
    case _:
        print("Wrong Color!")