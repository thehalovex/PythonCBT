ages = {"Ben":35, "Joe":37, "Sally":22, "Jeff":18}
print(ages)
x = list(ages)

newKey = input("Please enter the key to change: ")
raw_newVal = input("Please enter the value to change: ")
newVal = int(raw_newVal)

ages[newKey] = newVal
print(ages)

newKey = input("Please enter a new key to add: ")
raw_newVal = input("Please enter a new value to add: ")
newVal = int(raw_newVal)

ages[newKey] = newVal
print(ages)

remKey = input("Please enter a key to remove: ")
if remKey != x:
	print('That Key does not exist. Try again...')
	remKey = input("Please enter a key to remove: ")
else:
	del ages[remKey]
print(ages)