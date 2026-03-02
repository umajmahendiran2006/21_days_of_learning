
n=int(input('enter a number: '))

res=[]
for i in str(n):
	res.append(int(i)**3)

if sum(res)==n:
	print('Armstrong number')
else:
	print('not a Armstrong number')	