class vehicle:
	def start(self):
		pint("vehicle is stating...")
class car(vehicle):
	def start(self):
		print("car starts with key")
class bike(vehicle):
	def start(self):
		print("ike starts with kick")
c=car()
b=bike()
c.start()
b.start()		