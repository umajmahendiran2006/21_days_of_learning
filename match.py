a=10;
b=5;
op=input("enter the operator('+','-','*','/':")
match op:
	case "+":
		print(a+b)
	case '-':
		print(a-b)
	case '*':
		print(a*b)
	case '/':
		print(a/b)
	case _ :
		print("enter the vaild input")



