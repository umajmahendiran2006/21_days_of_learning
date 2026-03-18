total_seats=40
while total_seats>0:
	print("available seats:",total_seats)
	booking=int(input("enter the number of seats you need: "))
	if booking<=0:
		print("please enetr a valid number of seats")
	elif booking<=total_seats:
		total_seats-=booking
		print("booked successfully")
	else:
		print("not enough seats available")	
print("all seats are booked")		