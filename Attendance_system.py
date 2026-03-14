attendance=["p","p","p","a","a","p","p","a","p","p","p","p","p"]
present=0
absent=0
for i in attendance:
	if i=="p":
		present+=1
	else:
		absent+=1
total=len(attendance)
percentage=(present/total)*100
print("present:",present)
print("absent:",absent)
print("attendance percentage:",percentage)
if percentage>=75:
	print("attendance percentage is above 75%")			
else:
	print("attendance percentage is below 75%")	