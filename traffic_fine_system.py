def calculate_fine(no_helmet,no_license,overspeed):
	fine=0
	if no_helmet:
		fine+=500
	if no_license:
		fine+=1000
	if overspeed:
		fine+=1500
	return fine
helmet=input("no helmet?(yes/no):").lower()=="yes"
license=input("no license?(yes/no):").lower()=="yes"
speed=input("overspeed?(yes/no):").lower()=="yes"
total_fine=calculate_fine(helmet,license,speed)
print(f"total_fine: {total_fine}")