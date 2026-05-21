def subsets(arr):
	result=[[]]
	for i in arr:
		result+=[j+[i] for j in result]
	return result
print(subsets([1,2,3]))		