'''Write a Python program to input marks for five subjects Physics,
Chemistry, Biology, Mathematics, and Computer. Calculate the
percentage and grade according to the following:
Percentage >= 90% : Grade A
Percentage >= 80% : Grade B
Percentage >= 70% : Grade C
Percentage >= 60% : Grade D
Percentage >= 40% : Grade E
Percentage < 40% : Grade F'''

print("Enter the marks for the following subjects")
Phy=int(input("Enter the marks for Physics:"))
Che=int(input("Enter the marks for Chem:"))
Bio=int(input("Enter the marks for Bio:"))
Math=int(input("Enter the marks for Math:"))
Comp=int(input("Enter the marks for Comp:"))
total=Phy+Che+Bio+Math+Comp
Percentage=(total/500)*100

if Percentage >= 90:
 print("Grade A")
elif Percentage >= 80:
    print("Grade B")
elif Percentage>=70:
    print("Grade C")
elif Percentage >= 60:
    print("Grade D")
elif Percentage>=50:
    print("Grade E")
elif Percentage<=40:
    print("Grade F")
else:
    print("Invalid input")

print(Percentage)