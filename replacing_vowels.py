s=input("enter the string: ")
vowels="aeiou"
res=""
s=s.lower()
for i in s:
	if i in vowels:
		res+="*"
	else:
		res+=i
print(res)			