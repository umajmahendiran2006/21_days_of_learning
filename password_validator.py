password=input('enter your password: ')
upperCase="QWERTYUIOPLKJHGFDSAZXCVBNM"
lowercase="qwertyuioplkjhgfdsazxcvbnm"
special_char="!@#$%^&*"

upper=False
lower=False
special=False
digit=False
for i in password:
	if i in upperCase:
		upper=True
	if i in lowercase:
		lower=True
	if i in special_char:
		special=True
	if i.isdigit():
		digit=True
if len(password)>=8 and upper and lower and special	and digit:
	print("Valid password")
else:
	print("invalid password")					
	