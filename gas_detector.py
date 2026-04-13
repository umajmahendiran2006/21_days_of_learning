import random
import time

while True:
	gas_level=random.randint(0,100)
	print("gas_level:", gas_level)
	if gas_level>70:
		print("gas leakage detected")
	else:
		print("safe")
	print("-----------")
	time.sleep(2)		
