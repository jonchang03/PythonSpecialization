# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fname = input("Enter file: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)

hourCounts = dict()
for line in fh :
    line = line.rstrip()
    if not line.startswith('From ') : continue 
    words = line.split()
    time = words[-2]    # time is the second to last string in the line
    hour, minute, second = time.split(':')  # split the string using the colon as the separator
    # print(hour)
    hourCounts[hour] = hourCounts.get(hour, 0) + 1

# get a sorted list of tuples
for k, v in sorted(hourCounts.items()) :
    print(k, v)