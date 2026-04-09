arr=[10,20,30,40,50]
key=10
found=False
for i in range(len(arr)):
	if arr[i]==key:
		print("element found at index:", i)
		found=True
		break
if not found:
	print("element not found")		