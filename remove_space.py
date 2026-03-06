string=str(input("enter the string: "))
res=[]
for i in string:
	if i!=" ":
		res.append(i)
print("".join(res))