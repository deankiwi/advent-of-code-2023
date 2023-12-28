import re

filename = r'tast-1-data.txt'
count = 0
regex = "\d"

with open(filename) as file:
    for line in file:
        arrayNum = re.findall(regex,line)
        # addNum = int(''.join(re.findall(regex,line)))
        # count +=  int(''.join(re.findall(regex,line)))
        print( arrayNum, end='    ')

        count += int(arrayNum[0] + arrayNum[-1])
 
    print( count)
