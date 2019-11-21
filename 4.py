
# 4. Conversion of minutes to time

N= int(input("Enter the time passes in minutes:"))
h= int(N/60)
print("The time displayed on the clock is "+ str(h)+":"+str(int(N-h*60)))