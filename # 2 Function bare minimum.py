# 2 Function bare minimum


def fizz_buzz(n) :
    if n%3 == 0:
        print("Fizz")
    elif n%5 == 0:
        print("Buzz")
    elif n%3 ==0 and n%5==0:
        print("FizzBuzz")
    else:
        print(n)
    return

fizz_buzz(int(input("Enter a number: ")))