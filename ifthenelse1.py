name = input('Please tell me your name: ')
rawAge = input('Please tell me your age: ')
age = int(rawAge)

if age >= 20:
	print(name, 'you are allowed in!')
	print('What would you like to drink?')
else:
	print('Unfortunately', name, 'you are not allowed in.')
