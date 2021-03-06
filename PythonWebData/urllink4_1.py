# Scraping Numbers from HTML using BeautifulSoup
# In this assignment you will write a Python program similar to http://www.pythonlearn.com/code/urllink2.py.
# The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers
# nd compute the sum of the numbers in the file.


# Sample data: http://python-data.dr-chuck.net/comments_42.html (Sum=2553)
# Actual data: http://python-data.dr-chuck.net/comments_197759.html (Sum ends with 51)
import urllib.request
from bs4 import BeautifulSoup
import re

url = input('Enter - ')
if len(url) < 1 : url = "http://python-data.dr-chuck.net/comments_197759.html"
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, "lxml")


# Retrieve all of the span tags
tags = soup('span')
# empty list to add
numberList = list()
for tag in tags:
    # Look at the parts of a tag
    # print('TAG:',tag)
    # print('URL:',tag.get('href', None))
    # print('Contents:',tag.contents[0])
    # print('Attrs:',tag.attrs)
    numberList += re.findall('^[0-9]+$', tag.contents[0]) # findall returns a list of the one number per line

# conver list of strings to list of ints using list comprehension
numberList = [int(i) for i in numberList]
print(numberList)
print(sum(numberList))
