n=input('enter a string: ');
n.lower()
result=[]
vowel=['a','e','i','o','u']
for i in n:
	if i not in vowel:
		result.append(i)
print("".join(result)) 