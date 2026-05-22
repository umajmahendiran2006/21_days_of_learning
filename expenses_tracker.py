expenses=[]
n=int(input("enter number of expenses: "))
for i in range(n):
	amount=float(input('enter the expense amount: '))
	expenses.append(amount)
total=sum(expenses)
print("expenses: ",expenses)
print("Total expense=",total)	