def computepay(h,r):
    if h <= 40:
        pay = h * r
    elif h > 40:
        pay = (40 * r) + (h-40)*(1.5 * r)
    return pay
    
hours = raw_input("Enter hours:")
rate = raw_input("Enter rate:")

hours = float(hours)
rate = float(rate)

print computepay(hours,rate)