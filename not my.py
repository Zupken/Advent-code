# http://adventofcode.com/2017/day/2/input
input = []
with open('day2.txt','r') as f:
    for line in f:
        inputline = []
        for word in line.split():
            inputline.append(word)

        input.append(inputline)

#---------------Solution 1--------------#
# http://adventofcode.com/2017/day/2

number = ""
sum = 0
for x in range(len(input)):
    max = 0
    min = 10000
    row = str(input[x])
    for y in range(len(row)):
        try:
            char = int(row[y])
            number += str(char)

        except ValueError:
            try:
                mm = int(number)
                if (mm > max):
                    max = mm
                if (mm < min):
                    min = mm
                number = ""
            except ValueError:
                number = ""

    print(min, max)
    sum += (max - min)
    print(sum)