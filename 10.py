
# 10. Conversion to seconds to day, hours, minutes and seconds

n = int(input("Enter the seconds: "))

day = int(n / (24 * 60 * 60))
n = n % (24 * 60 * 60)
hour = int(n / (60 * 60))
n = n % (60 * 60)
minutes = int(n / 60)
n = n % 60
seconds = n

print('The given seconds in Day:Hour:Minute:Second is %d:%d:%d:%d' % (day, hour, minutes, seconds))
'''