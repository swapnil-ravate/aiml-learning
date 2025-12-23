'''
12. break Statement
------------------
Used to terminate the loop immediately.

#Example -

i = 1

while (i <= 10):
    if(i % 6 == 0):
        break
    print(i)
    i += 1
print("Outside loop now...")

'''



'''
12. continue Statement
---------------------
Used to skip the current iteration.
'''

i = 1

while (i <= 10):
    if(i % 3 == 0):
        i += 1
        continue
    print(i)
    i += 1
print("outside loop...")