num = 17

for test in range(2,num):

	if num % test == 0 and num != test:
		print(num, 'equals', test, '*', num/test)
		print(num, 'is not a prime number')
		prime = False
		break
else:
	print(num, 'is a prime number')
