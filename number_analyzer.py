num=int(input("enter the number: "))
#prime number
if num<=1:
	print("not a prime number")
for i in range(2,num):
	if num%i==0:
		a=" not a prime number"
		break
	else:
		a="prime number"
print(a)

#palindrome

temp=num
rev=0
while temp>0:
	digit=temp%10
	rev=rev*10+digit
	temp=temp//10
if rev==num:
	print("palindrome")
else:
	print("not a palindrome")		

#armstrong


res=[]
for i in str(num):
	res.append(int(i)**3)

if sum(res)==num:
	print('Armstrong number')
else:
	print('not a Armstrong number')	

