import urllib.request, urllib.parse, urllib.error

hand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt') #Read the lines in a text file

counts = dict()

for line in hand : 
	words = line.decode().split()
	for word in words : 
		counts[word] = counts.get(word, 0) + 1
		
print(counts)