arr=[3,1,2]
swaps=0
comparisons=0
for i in range(len(arr)):
	for j in range(len(arr)-1):
		comparisons+=1
		if arr[j]>arr[j+1]:
			arr[j],arr[j+1]=arr[j+1],arr[j]
			swaps+=1
print("swaps",swaps)
print("comparisons",comparisons)			