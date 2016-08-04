#exercise 8-4
fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    test = line.split()
    for word in test:
        if word in lst: continue
        lst.append(word)
lst.sort()
print lst