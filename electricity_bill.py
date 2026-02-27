units=int(input('enter the electricity units:'))
bill=0
if units<=100:
	bill=units*5
elif units>100 and units <=200 :
	bill=units*6
elif units >200 and units<=500:
	bill=units*7
else:
	bill=units*8
print("your electricity bill is:",bill)		
