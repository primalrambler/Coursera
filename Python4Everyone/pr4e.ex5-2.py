largest = None
smallest = None

while True:
	num = raw_input("Enter a number: ")
	
	if num == 'done' : break
	
	try:
		num = int(num)
	except:
		print 'Invalid input'
		continue

	if largest is None:
		largest = num
	if smallest is None:
		smallest = num
	
	if num > largest:
		largest = num
	if num < smallest:
		smallest = num

print type(num)
print type(largest)
print type(smallest)
print "Maximum is", largest
print "Minimum is", smallest