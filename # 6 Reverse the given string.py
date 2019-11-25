# 6 Reverse the given string

string = input("Enter a string you want to reverse: ")
newStr=""
for i in range(len(string)-1,-1,-1):
    newStr += string[i]
print("The reversed string is :", newStr)