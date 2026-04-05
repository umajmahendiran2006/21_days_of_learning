cart={}
while True:
	print("1.add  2.remove  3.total  4.exit")
	choice=input("enter choice: ")
	if choice=="1":
		item=input("item name: ")
		price=float(input("price: "))
		cart[item]=price
	elif choice=="2":
		item=input("item to remove: ")
		cart.pop(item,None)
	elif choice=="3":
		total=sum(cart.values())
		print("total price:",total)
	elif choice=="4":
		break			