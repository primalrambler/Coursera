#Exercise 9.4
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
text = list()
names = list()
counts = dict()

#create a list of the names
for line in handle:
    if line.startswith("From "):
        text = line.split()
        names.append(text[1])

#count the names
for name in names:
     counts[name] = counts.get(name,0) +1

# find the name with the highest count
bigname = None
bigcount = None

for name,count in counts.items():
    if bigcount is None or count > bigcount:
        bigname = name
        bigcount = count

print bigname, bigcount