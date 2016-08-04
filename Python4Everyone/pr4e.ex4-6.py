def computepay(h,r):
    if h > 40:
        return (40*r) + (h-40)*(r*1.5)
    else:
        return h * r  

hrs = raw_input("Enter Hours:")
h = float(hrs)

rate = raw_input("Enter Hourly Rate:")
r = float(rate)

pay = computepay(h,r)
print pay