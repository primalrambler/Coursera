fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fhand = open(fname)
count = 0

for line in fhand:
	line = line.rstrip()
	if line == []:continue
	if 'From ' in line:
		temp = line.split()
		print temp[1]
		count = count +1

print "There were", count, "lines in the file with From as the first word"