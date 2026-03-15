string=str(input("enter the string: "))
upper_count=0
lower_count=0
for i in string:
	if i.isupper():
		upper_count+=1
	else:
		lower_count+=1	
print("upper_count =",upper_count)
print("lower_count =",lower_count)		