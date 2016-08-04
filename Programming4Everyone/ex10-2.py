name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

time = list()
hours = list()
counts = dict()


for line in handle:
    line = line.rstrip()
    if line == []:continue
    if 'From ' in line:
        line = line.split()
        time.append(line[5])

for hour in time:
	hour = hour.split(":")
	hours.append(hour[0])

for hour in hours:
	counts[hour] = counts.get(hour,0)+1

tmp = counts.items()
tmp.sort()

for k,v in tmp:
	print k, v
