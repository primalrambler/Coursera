# Use words.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
#flines = fh.read()

for line in fh:
    line = line.rstrip()
    line = line.upper()
    print line