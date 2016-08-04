#problem 10.2
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"


#variables
handle = open(name)
text = list()
time = list()
hours = list()
counts = dict()
countList = list()


#isolate the hour and create a list of hours
for line in handle:
    if line.startswith("From "):
        text = line.split()
        temp = text[5]
        time = temp.split(':')
        hours.append(time[0])

#count the hours
for hour in hours:
     counts[hour] = counts.get(hour,0) +1

countList = sorted(counts.items())

for h,c in countList:
    print h, c