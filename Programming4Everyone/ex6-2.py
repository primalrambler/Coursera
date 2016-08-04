text = "X-DSPAM-Confidence:    0.8475";
#PREVIOUS VERSION
#blank_pos = text.find(" ")
#print blank_pos
#num_text = text[blank_pos:]
#print num_text
#num_text = num_text.strip()
#print num_text
#num_val = float(num_text)
#print num_val

#REFACTORED version

pos = text.find(':')
num = float(text[pos +1:])
print num