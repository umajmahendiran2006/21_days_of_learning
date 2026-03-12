#rotating right
arr=[1,2,3,4,5,6]
last=arr[-1]
for i in range(len(arr)-1,0,-1):
	arr[i]=arr[i-1]
arr[0]=last
print(arr)



#rotaing left
arr=[1,2,3,4,5,6]
first=arr[0]
for i in range(len(arr)-1):
	arr[i]=arr[i+1]
arr[len(arr)-1]=first
print(arr)	