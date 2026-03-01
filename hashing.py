n=input('enter a string: ')
frequency={}
for i in n:
	if i in frequency:
		frequency[i]+=1
	else:
		frequency[i]=1
print("character frequency")
for key,value in frequency.items():
	print(key,":" ,value)	