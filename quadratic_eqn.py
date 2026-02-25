import math
a=int(input('enter the co-efficient of a:'))
b=int(input('enter the co-efficient of b:'))
c=int(input('enter the co-efficient of c:'))
d=b**2-(4*a*c)
if d>0:
	x1=(-b + math.sqrt(d))/(2*a)
	x2=(-b - math.sqrt(d))/(2*a)
	print('the roots are distinct')
	print(x1)
	print(x2)
elif d==0:
	x=-b/(2*a)
	print('the roots are equal')
	print(x)
else:
	real_part=-b/(2*a)
	imag_part=math.sqrt(-d)/(2*a)	
	print('the roots are complex')
	print(f"{real_part}+{imag_part}i")
	print(f"{real_part}-{imag_part}i")

