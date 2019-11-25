# 4 sum of multiple of 3,5 on limit
def limit(number):
    for x in range(number + 1):
        sum=0
        if x % 3 == 0 or x % 5 == 0:
            sum += x
    return sum


number = int(input("Enter a number: "))
print("The sum is ",limit(number))

