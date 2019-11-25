# 2 Print the result

firstSub= int(input("Enter the marks of first subject: "))
secondSub= int(input("Enter the marks of second subject: "))
thirdSub= int(input("Enter the marks of third subject: "))
fourthSub= int(input("Enter the marks of fourth subject: "))
total =firstSub+secondSub+thirdSub+fourthSub
print("The total marks is: ",total)

percentage= total/4

print("The percentage is ",percentage)
if percentage>70:
    print("Distinction")
elif percentage>60:
    print("First division")
elif percentage>40:
    print("Pass")
else:
    print("Fail")
