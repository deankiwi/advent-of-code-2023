import re

filename = r'tast-1-data.txt'
count = 0
regex = "\d"
numletter = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine' : '9',
    '1' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9

}

sizes = [1,3,4,5]



with open(filename) as file:


    for line in file:
        array = []
        print('word is --> ',line)
        for x in range(len(line)):
            for y in sizes:
                if y == 1:
                    print(line[x])
                    if line[x] in numletter:
                        array.append(line[x])
                    if x+y >= len(line)-1:
                        print('< --- broken')
                        break

                    # check for digit
                    pass
                else:
                    print(line[x:min(x+y,len(line))])
                    if line[x:min(x+y,len(line))] in numletter:
                        array.append(numletter[line[x:min(x+y,len(line))]])
     
                    if x+y >= len(line)-1:
                        print('< --- broken')
                        break
        print(array, '<- line array')
    
        print( int(array[0] + array[-1]),'<- this is sum of line')

        count += int(array[0] + array[-1])
        
        # print( arrayNum, '   ', ' ->', int(arrayNum[0] + arrayNum[0]), '<- addcount->',count)
 
    print( count)
