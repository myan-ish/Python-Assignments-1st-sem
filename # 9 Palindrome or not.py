# 9 Palindrome or not
def palin(string):
    newStr = ""
    for i in range(len(string) - 1, -1, -1):
        newStr += string[i]
    if newStr == string:
        print("The string is palindrome.")
    else:
        print("The string is not palindrome.")

palin(input("Enter a string you want to reverse: "))