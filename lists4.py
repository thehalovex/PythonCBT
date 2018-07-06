names = ["Ben", "Sally", "Amy", "George", "Randy", "Alice"]

#x = names.index("George")
#print(x)

for index in range(0,len(names)):
	print(names[index], 'is found at index:',index)

for name in names:
	print(name, 'is found at index:', names.index(name))