arr=[1,2,3,5]
n=len(arr)+1
total_sum=n*(n+1)//2
arr_sum=sum(arr)
missing=total_sum-arr_sum
print(missing)
