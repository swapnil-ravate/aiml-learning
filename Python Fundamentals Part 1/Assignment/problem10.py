# Q10: Take a decimal number as input (like 45.78) and print:
#       • integer part  → 45
#       • fractional part → 0.78

num = float(input("Enter a decimal Num :"))

int_part = int(num)
fractional_part = num - int_part

print("Integer Part :", int_part)
print("Fractional Part:", fractional_part)
