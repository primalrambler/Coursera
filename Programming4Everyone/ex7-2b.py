# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fhand = open(fname)
count = 0
tot_val = 0
for line in fhand:
	if not line.startswith("X-DSPAM-Confidence:") : continue
	count = count + 1
	blank_pos = line.find(" ")
	num_text = line[blank_pos:]
	num_text = num_text.strip()
	tot_val = tot_val + float(num_text)
    
avg_val = tot_val/count
print "Average spam confidence:",avg_val
print count


