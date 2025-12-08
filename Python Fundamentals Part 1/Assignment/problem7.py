# Q7: Ask the user for a temperature in Celsius (string input).
#     Convert it to float, calculate, and print temperature in Fahrenheit.
#     Formula: Fahrenheit = (Celsius * (9/5)) + 32


temp = str(input("Enter Temp : "))

temp = (float(temp))
print(temp,"C")

# temp Conversion formula
fahrenheit_temp = (temp * (9/5)) + 32

print("Temp in Fahrenheit :",fahrenheit_temp)