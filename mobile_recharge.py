price=int(input("enter the total price: "))
if price>=500:
	print("20% cashback")
	total_price=price*(20/100)
	print(price-total_price)
elif price>=200:
	print("10% cashback")
	total_price=price*(10/100)
	print(price-total_price)
else:
	print("no cashback")
	print(price)		