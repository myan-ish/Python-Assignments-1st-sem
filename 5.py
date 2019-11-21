# 5. Smallest number of desk required

a=int(input("Enter the number of students in the first class, a: "))
b=int(input("Enter the number of students in the second class, b: "))
c=int(input("Enter the number of students in the third class, c: "))

inFirstClass = int(a/2)
inSecondClass =int(b/2)
inThirdClass =int(c/2)

flotNumbers = ((a/2)-int(a/2))*2 + ((b/2)-int(b/2))*2+ ((c/2)-int(c/2))*2
total = inFirstClass+ inSecondClass + inThirdClass + flotNumbers
print("Total number of desks required is ", total)
