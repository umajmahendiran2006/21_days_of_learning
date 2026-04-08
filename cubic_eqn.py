def cubic(x,a,b,c,d):
	return a*x**3+b*x**2+c*x+d
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = int(input("Enter d: "))
print("the roots are")
for i in range(-10,11):
	if cubic(i,a,b,c,d)==0:
		print("root is:",i)