

class Solution:
    def __init__(self):
        self.number_pairs = 0

    def search_pairs(self, line):
        list = line.strip().split(' ')
        for index, name in enumerate(list):
            for i in list[index+1:]:
                if name == i:
                    self.number_pairs += 1
                    return True


myfile = open('day4.txt', 'r')
Solution = Solution()
for line in myfile.readlines():
    Solution.search_pairs(line)
# Solution.search_pairs('gjtszl gjtszl fruo fruo')
print(512 - Solution.number_pairs)


