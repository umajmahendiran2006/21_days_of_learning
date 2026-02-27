balance=17000
withdraw=int(input('enter the withdrawal amount:'))
if withdraw >20000:
	print("tTransaction failed due to limit exceed")
elif withdraw>balance:
	print("tTransaction fsiled due to withdraw exceed the balance")
else:
	balance=balance-withdraw
	print("tTransaction successful! Remaining balace:",balance)		