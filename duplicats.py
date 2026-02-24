n=input('enter the input: ');
res=[]
for i in n:
	if i not in res:
		res.append(i)
print("".join(res))		