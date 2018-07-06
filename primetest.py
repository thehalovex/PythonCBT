num = input('Test a number: ')
prime = True

for test in range(2,1000):

	if int(num) % test == 0 and int(num) != test:
		print(int(num), 'equals', test, '*', int(num)/test)
		prime = False

if prime:
	print(int(num), 'is a prime number!')
else:
	print(int(num), 'is not a prime number')