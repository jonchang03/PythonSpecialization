# In this assignment you will write a Python program somewhat similar to http://www.pythonlearn.com/code/geoxml.py.
# The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract
# the comment counts from the XML data, compute the sum of the numbers in the file.
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing
# and the other is the actual data you need to process for the assignment.
# Sample data: http://python-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://python-data.dr-chuck.net/comments_197756.xml (Sum ends with 43)

import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter url: ')
if len(url) < 1 : url = 'http://python-data.dr-chuck.net/comments_197756.xml'
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()

print('Retrieved',len(data),'characters')
tree = ET.fromstring(data)
lst = tree[1].findall('comment')
#print(len(lst))
total = 0
for item in lst:
    print('Count', item.find('count').text)
    total += int(item.find('count').text)
print(total)
