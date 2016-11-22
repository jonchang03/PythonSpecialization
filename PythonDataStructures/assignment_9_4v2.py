# 9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the 
# greatest number of mail messages. The program looks for 'From ' lines and takes the second word 
# of those lines as the person who sent the mail. The program creates a Python dictionary that maps 
# the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop 
# to find the most prolific committer.

fname = input("Enter file: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)

# look for 'From ' lines and take the 2nd word (email addresses) of these lines and append it to emailList
emailCounts = dict()
for line in fh :
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    email = words[1]
    # use emailCounts dictionary to keep track of how many times each email addresses appears
    emailCounts[email] = emailCounts.get(email, 0) + 1

# loop through the dictionary to find the most profilic committer
profilic_committer = 'email'
largest = -1
for key, value in emailCounts.items() :
    if value > largest :
        largest = value
        profilic_committer = key

print(profilic_committer, largest)



