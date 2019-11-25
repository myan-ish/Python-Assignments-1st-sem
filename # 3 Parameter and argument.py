# 3 Parameter and argument

def showNumber(limit):
    for x in range(limit):
        if x % 2 == 0:
            print("%d Even" % (x))
        else:
            print("%d Odd" % (x))
    return
limit = int(input("Enter a number: "))
showNumber(limit)


