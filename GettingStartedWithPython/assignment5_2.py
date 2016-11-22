# Input from Exercise 5.1
# 4, 5, bad data, 7, done
largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    # If the user enters anything other than a valid number catch it with a 
    # try/except and put out an appropriate message and ignore the number. 
    if num == "done" : 
        break
    try:
        num = int(num)            
        if largest is None :
            largest = num
        elif num > largest :
            largest = num
        if smallest is None :
            smallest = num
        elif num < smallest :
            smallest = num
    except:
        print "Invalid input"
        continue

print "Maximum is", largest
print "Minimum is", smallest