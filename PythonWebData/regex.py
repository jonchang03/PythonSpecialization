# The basic outline of this problem is to read the file, look for integers using the re.findall(), 
# looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.

import re

fname = input("Enter file: ")
if len(fname) < 1 : fname = "regex_sum_197754.txt"
fh = open(fname)

fileLine = fh.read() # read the whole file into a single string
int_string = re.findall('[0-9]+', fileLine)
print(int_string)

# list comprehension to convert list of strings to list of ints
intList = [int(i) for i in int_string]
print(sum(intList))


