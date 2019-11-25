# 8 Find sum of the given digits
sum=0
x = input("Enter a three digit number: ")
for i in range(len(x)):
    sum += int(x[i])
print("The sum of the digits is ", sum)

