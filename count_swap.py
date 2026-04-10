arr=[9,2,4,6]
n=len(arr)
swaps=0
comparison=0
for i in range(n):
	for j in range(0,n-i-1):
		comparison+=1
		if arr[j]>arr[j+1]:
			arr[j],arr[j+1]=arr[j+1],arr[j]
			swaps+=1
print("sorted array ",arr)	
print("number of comparisons: ",comparison)
print("number of swaps: ",swaps)		