current=int(input("enter current hour(0-23): "))
alaram =int(input("enter the alarm hour(0-23): "))
if alaram>=current:
	time_left=alaram-current
else:
	time_left=(24-current)+alaram
print("hours left for alarm",time_left)	