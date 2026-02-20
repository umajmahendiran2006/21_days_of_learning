import random
A=[1,2,3,4,5]
x=random.choice(A);
for i in range(0,3):
	y=int(input('enter a random number: '));
	if x==y:
		print('you won the game')
	else:
		print('better luck next time')	