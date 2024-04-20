import re

hand = open('mbox-short.txt')

for line in hand :
    y = re.findall('^From: .*@([^ ]*\S)',line) # Lines starting with 'From: ' with any number of characters leading to an '@', it extracts any number of non white space characters, and prints it.
    if y : print(y)