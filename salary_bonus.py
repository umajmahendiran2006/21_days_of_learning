salary=int(input("enter your salary: "))
if salary>=50000:
	bonus=salary*0.20
elif salary>=30000:
	bonus=salary*0.10
else:
	bonus=salary*0.05
print("bonus= ",bonus)			