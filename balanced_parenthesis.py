def is_balanced(s):
	stack=[]
	for i in s:
		if i=="(":
			stack.append(i)
		elif i==")":
			if not stack:
				return "invalid" 
			stack.pop()
	if not stack:
		return "valid"				
	else:
		return "invalid"	
print(is_balanced("(((((())))))"))		
