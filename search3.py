import re

hand = open('mbox-short.txt')

for line in hand :
    line = line.rstrip()
    if re.search('^X.*: ', line) : print(line)