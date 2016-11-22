def computepay(h,r):
    if h < 40 :
        pay = h * r
    else :
        # Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate 
        # for all hours worked above 40 hours.
        pay = 40 * r + (h - 40) * 1.5 * r
    return pay
hrs = raw_input("Enter Hours:")
hrs = float(hrs)
rate = raw_input("Enter Rate:")
rate = float(rate)

p = computepay(hrs,rate)
print p