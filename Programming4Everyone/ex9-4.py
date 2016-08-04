fname = raw_input("Enter file:")
if len(fname) < 1 : fname = "mbox-short.txt"
handle = open(fname)
mail = list()
counts = dict()


for line in handle:
    line = line.rstrip()
    if line == []:continue
    if 'From ' in line:
        line = line.split()
        mail.append(line[1])

for address in mail:
    counts[address] = counts.get(address,0) + 1

print counts

bigcount = None
bigcomment = None

for address,count in counts.items():
     if bigcount is None or count > bigcount:
        bigcount = count
        bigcomment = address

print bigcount
print bigcomment