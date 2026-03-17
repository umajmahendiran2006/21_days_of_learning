parking_time=int(input("enter the parking time: "))
fee=0
if parking_time<=2:
	fee=parking_time*20
elif parking_time<=5:
	fee=(2*20)+((parking_time-2)*30)
else:
	fee=(2*20)+(3*30)+((parking_time-5)*50)
print("parking fee",fee)	