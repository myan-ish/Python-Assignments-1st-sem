# 10 Sum of integer with a twist

a= int(input("Enter the first number: "))
b= int(input("Enter the second number: "))
c= int(input("Enter the third number: "))

sum = a+b+c

if a==b or a==c or b==c:
    sum=0

print("The sum is",sum)
