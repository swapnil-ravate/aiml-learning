'''
11. Loops
---------
A loop is used to execute a block of code repeatedly.

Python provides:
- while loop
- for loop

# Agar kisi task ko ham bar bar repeat karna chahte hai to loop ka use kiya jaata hai.
'''

'''
11. While Loop
--------------
A while loop executes code as long as a condition is True.

Syntax:

while condition:
    code

    
    # while loop - jb tak koi condition true value return nahi karti tab tak loop repeat hota rehta hai. its work with counter and iterator variable
'''


'''
11. Infinite Loop
----------------
Occurs when the condition never becomes False.
Avoid infinite loops unless intentionally required.

# Example (DO NOT RUN unless needed)
while True:
    print("Heyyy!")
'''

# finite loop
i = 1 #iterator like i j k

while (i <= 10):
    print("Heyyy!", i)
    i += 1
print("After loop, count = ", i) #11


'''
11. When to Use while Loop
-------------------------
- Number of iterations is unknown
- User input based programs
- Retry mechanisms
- Game loops
'''