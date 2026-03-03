s=input('enter a string: ').lower()
alphabets="qwertyuioplkjhgfdsazxcvbnm"
for i in alphabets:
	if i not in s:
		print("the string is not a pangram")
		break
	else:
		print("the stringis a pangram")		