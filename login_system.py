username="admin"
password="1234"
attempts=3
while attempts>0:
	user_name=input("enter username:")
	pass_word=input("enter the pass_word:")
	if user_name==username and pass_word==password:
		print("login successful")
		break
	else:
		attempts-=1
		print("wrong credentials")
		print("attempts left:",attempts)
if 	attempts==0:
	print("account locked")		