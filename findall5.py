import re

hand = open('mbox-short.txt')

numList = list()

for line in hand :
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line) # Extract the number that starts with a number between 0 and 9, followed by a decimal.
    if len(stuff) != 1 : continue #If there isnt a successful extraction, skip.
    num = float(stuff[0])
    numList.append(num)
	
print('Maximum: ', max(numList))