import re

handle = open('regex_sum_2003771.txt')

numList = list()

total = 0

for line in handle :
    line = line.rstrip()
    nums = re.findall('[0-9]+',line)
    if len(nums) == 0 : continue
    for num in nums : total += int(num)
		
print(total)