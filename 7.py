# 7. Time problem

distance = 4
speedOfBus = 25
timeSpentOnStops = 2
numberOfStops = 10
yourSpeedForFirst = 7
yourSpeedForNextTwo = 15
yourSpeedForLast = 7

timeTakenByBus = ((1/speedOfBus)*distance)*60 + timeSpentOnStops*numberOfStops

timeTakenByYou = ((1/yourSpeedForFirst)+(2/yourSpeedForNextTwo)+(1/yourSpeedForLast))*60

if timeTakenByBus<timeTakenByYou:
    print("You are slower than the bus.")
else:
    print("You are faster than the bus.")

