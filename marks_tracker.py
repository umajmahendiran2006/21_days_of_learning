names=[]
marks=[]
n=int(input("enter the number of students: "))
for i in range(n):
	name=input("enter the student name: ")
	mark=input("enter the student mark: ")
	names.append(name)
	marks.append(mark)
print("students marks")
for i in range(n):
	print(names[i],":",marks[i])
highest=max(marks)
index=marks.index(highest)
print("topper: ",names[index])
print("highest marks: ",highest)	