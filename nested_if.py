Age=int(input('enter your age: '));
CitizenShip=input('you are a indian (y/n):').lower()
if CitizenShip=='y' or CitizenShip== 'yes':
	if Age>=18:
		print('You are eligible for voting')
	else:
		print('You age is not sufficient to vote')
else:
	print('You are not a indian citizen to vote')			