sum = 0
add = 10 

for x in range(1,add):
	print('The current sum is:',sum)
	print('How much would you like to add?', end ='')
	raw_add = input('(Type 0 to end the program): ')
	add = int(raw_add)
	sum = sum + add
	x = 1
	if add == 0:
		break
