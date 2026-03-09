total_amount=int(input("enter your total amount: "))
if total_amount>5000:
	print("20% discount")
	final_price=total_amount*(20/100)
	print(total_amount-final_price)
elif total_amount>2000 and total_amount<5000:
	print("10% discount")
	final_price=total_amount*(10/100)
	print(total_amount-final_price)	
else:
	print("no discount applicable")
	print(total_amount)