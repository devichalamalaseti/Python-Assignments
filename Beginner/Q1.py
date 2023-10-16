
'''If a number is divisible by 3 it should print “Consultadd” as a
string
If a number is divisible by 5 it should print “Python Training” as
a string
If a number is divisible by both 3 and 5 it should print
# “Consultadd - Python Training” as a string.'''
a=int(input("Enter the number"))
if a/3==0 and a/5==0:
    print("Consultadd")
elif a/3==0:
    print("Python Training")
elif a/5==0:
    print("Consultadd-Python Training")
else:
    print("Number is not divisible by 3 or 5")