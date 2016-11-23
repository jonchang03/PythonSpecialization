# The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags,
# scan for a tag that is in a particular position relative to the first name in the list, follow that link and
# repeat the process a number of times and report the last name you find.

# Sample problem: Start at http://python-data.dr-chuck.net/known_by_Fikret.html
# Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times.
# The answer is the last name that you retrieve.
# Sequence of names: Fikret Montgomery Mhairade Butchi Anayah

# Actual problem: Start at: http://python-data.dr-chuck.net/known_by_Gianluca.html
# Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times.
# The answer is the last name that you retrieve.
# Hint: The first character of the name of the last page that you will load is: D

import urllib.request
from bs4 import BeautifulSoup
import re

url = input('Enter URL: ')
if len(url) < 1 : url = "http://python-data.dr-chuck.net/known_by_Gianluca.html"

n = 7
# repeat process n+1 times (because we don't include the first time)
for x in range(0, n+1):
    print("Retrieving: ", url)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")

    # Retrieve all of the anchor tags
    tags = soup('a')

    position = 18
    for tag in tags:
        if not position == 1:
            position -= 1
            continue
        else:
            url = tag.get('href', None)
            break
