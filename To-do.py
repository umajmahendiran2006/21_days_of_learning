tasks=[]
while True:
	print("1.Add 2.view 3.exit")
	choice=input("enter the choice")
	if choice=="1":
		task=input("enter the task")
		tasks.append(task)
	elif choice=="2":
		for i in tasks:
			print(i)
	elif choice=="3":
		break		