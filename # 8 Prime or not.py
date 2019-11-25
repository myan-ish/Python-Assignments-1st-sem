# 8 Prime or not

def checker(number):
    for x in range(2,number):
        if number % x == 0:
            print("Not prime")
            break
        else:
            print("Prime")
            break


checker(int(input("Enter a number: ")))