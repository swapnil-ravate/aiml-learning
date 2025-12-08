# Q9: Ask the user to enter Principal (P), Rate (R), and Time (T).
# Convert all inputs to float and compute the Simple Interest.
# Formula: SI = (P * R * T) / 100


P = float(input("Enter Principal :"))
R = float(input("Enter Rate :"))
T = float(input("Enter Time :"))

SI = (P * R * T) / 100

print("Simple Interest is:", SI)