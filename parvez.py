import random

inArrivalTime =0
arrivalTime = 0

print('Customer no: \t\t Inter Arrival Time \t\t\t Arrival Time')

for i in range(1,21):
	if(i==1):
		print('%i \t\t\t\t\t - \t\t\t\t\t %i' % (i,arrivalTime))

	else:
		print('%i \t\t\t\t\t %i \t\t\t\t\t\t %i' % (i,inArrivalTime,arrivalTime))
	
	inArrivalTime = random.randrange(1,10)
	arrivalTime = inArrivalTime + arrivalTime