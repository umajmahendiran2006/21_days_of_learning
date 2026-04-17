import datetime
current_time=int(input("enter the current_time:"))
if current_time<12:
	print("good morning")
elif current_time<17:
	print("good afternoon")
elif current_time<20:
	print("good evening")
else:
	print("good night")			