#exercise 3-3

inp = raw_input("Enter a grade:")
grade = float(inp)

if grade >= 0.0 and grade <=1:
    if grade >= 0.9: print "A"
    elif grade >= 0.8: print "B"
    elif grade >= 0.7: print "C"
    elif grade >= 0.6: print "D"
    else: print "F"
else:
    print "Incorrect value"