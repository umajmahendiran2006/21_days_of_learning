l1=[10,11,12,13,14,15]
res=[]
result=[]
for i in l1:
	res.append(max(l1))
	for i in l1:
		if i not in res:
			result.append(i)
print(max(result))