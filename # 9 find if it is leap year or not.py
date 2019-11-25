# 9 find if it is leap year or not
year = int(input("Enter a year: "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("%d is a leap year"%(year))
       else:
           print("%d is not a leap year"%(year))
   else:
       print("%d is a leap year"%(year))
else:
   print("%d is not a leap year"%(year))

