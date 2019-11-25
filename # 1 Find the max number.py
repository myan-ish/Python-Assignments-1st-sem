# 1 Find the max number
def max(a,b,c):
    if a < b and c < b:
        biggest = b
    elif b < a and c < a:
        biggest = a
    else:
        biggest = c

    print("%d is the biggest number" % (biggest))

    return


biggest = 0

max(1,2,3)
