arr=[1,2,3,4,5,0,9,12,0,8]
result=[]
zero=[]

for i in arr:
	if i!=0:
		result.append(i)
	else:
		zero.append(i)
			
print(result+list(zero))			