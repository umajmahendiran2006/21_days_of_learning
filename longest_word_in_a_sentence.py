string=str(input("enter the string: "))
String=string.split()
longest_string=String[0]
for i in String:
	if len(i)>len(longest_string):
		longest_string=i
print(longest_string)	
