
# 4 Smallest integer

a= int(input("Enter the first number: "))
b= int(input("Enter the second number: "))
c= int(input("Enter the third number: "))
smallest = 0

if a>b and c>b:
    smallest = b
elif b>a and c>a:
    smallest =a
else:
    smallest = c

print("%d is the smallest number"%(smallest))
