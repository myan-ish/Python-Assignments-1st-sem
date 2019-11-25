# 7 Calulate the number of lower and uppercase

string = input("Enter a string: ")
x=len(string)-1
u=0
l=0
while x>=0:
    if string[x].isupper() == True:
        u+=1
    elif string[x].islower() == True:
        l+=1
    x-=1
print("The number of uppercased letter are ",u)
print("The number of lowercased letter are ",l)
