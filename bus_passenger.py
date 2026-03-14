passenger=[5,3,-2,4,-1,6,-6,7]
current=0
maximum=0
for i in passenger:
	current+=i
	if current>maximum:
		maximum=current
print("passenger remaining:",current)
print("maximum passenger at a time:",maximum)		