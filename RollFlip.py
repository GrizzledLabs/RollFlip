import random

print('Welcome to Roll & Flip by Grizzled Labs!\n')

while True:
	sides = input('\nHow many sides?   ')
	sideschecker = sides.isdigit()
	while sideschecker == False:
		sides = input('\nInvalid response...\nPlease enter number of sides:   ')
		sideschecker = sides.isdigit()
	if int(sides) > 2:
		modifier = input('\nAdd modifier? Y/N   ').upper()
		while modifier not in ('Y', 'N'):
			modifier = input('\nInvalid response\nAdd modifier? Y/N   ').upper()
		if modifier == 'Y':
			mod = input('\nEnter modifier:   ')
			modchecker = mod.isdigit()
			while modchecker == False:
				mod = input('\nInvalid response\nEnter modifier:   ')
				modchecker = mod.isdigit()
		else:
			mod = 0
	else:
		mod = 0
	for i in range(1):
		roll = random.randint(1, int(sides))
		mod_roll = int(roll) + int(mod)
		if int(sides) > 2:
			print(f'\nYou rolled a {str(mod_roll)}!')
		else:
			if mod_roll == 1:
				print('\nCoin says HEADS')
			else:
				print('\nCoin says TAILS')