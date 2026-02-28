n=int(input('enter the year: '))
if (n%400==0) or ((n%4==0) and (n%100!=0)):
	print('leap_year')
else:
	print('not a leap year')	