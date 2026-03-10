num=int(input("enter a number: "))
cube_root=round(num**(1/3))
if cube_root*cube_root*cube_root==num:
	print("it is a perfect cube")
else:
	print("not a perfect cube ")	