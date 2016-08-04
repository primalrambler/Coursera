fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
	line.rstrip()
	temp = line.split()
	#check to see if word is already in list
	#if it isn't add it to the list
	for w in temp:
		if w in lst : continue
		lst.append(w)
lst.sort()
print lst