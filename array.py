#print elements in array
arr=[10,20,30,40,50]
for i in arr:
	print(i)
#sum of elements
arr=[10,20,30,40,50]
sum=0
for i in arr:
	sum=sum+i
print(sum)	
#largest element
arr=[10,20,30,40,50]
largest=arr[0]
for i in arr:
	if i>largest:
		largest=i
print(largest)
#smallest
arr=[10,20,30,40,50]
smallest=arr[0]
for i in arr:
	if i<smallest:
		smallest=i
print(smallest)		
#count elemts without using len()
arr=[10,20,30,40,50]
count=0
for i in arr:
	count=count+1
print(count)	