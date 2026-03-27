a=input("enter the input: ")
frequency={}
for i in a:
	if i in frequency:
		frequency[i]+=1
	else:
		frequency[i]=1
for i in a :
	if frequency[i]==1:
		print(i)	
		break	