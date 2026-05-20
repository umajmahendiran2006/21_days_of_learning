plate_number=input("enter the plate number: ")
if (len(plate_number)==10 and plate_number[:2].isalpha() and plate_number[2:4].isdigit() and plate_number[4:6].isalpha() and plate_number[6:].isdigit()):
	print("Valid")
else:
	print("invalid")