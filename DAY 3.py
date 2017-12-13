# 38  36  35  34  33  32  31
# 39  17  16  15  14  13  30
# 39  18   5   4   3  12  29
# 40  19   6   1   2  11  28
# 41  20   7   8   9  10  27
# 42  21  22  23  24  25  26
# 43  44  45  46  47  48  49


class Solution:
    def __init__(self):
        self.basic_number = 0
        self.number = 2
        self.x = 0
        self.y = 0
        self.coordinates = {1: (0, 0)}

    def algorithm(self):
        while self.number <= 312051:
            self.x += 1
            self.save()
            while self.y != self.basic_number +1:
                self.y += 1
                self.save()
            while self.x != (-self.basic_number-1):
                self.x -= 1
                self.save()
            while self.y != (-self.basic_number -1):
                self.y -= 1
                self.save()
            while self.x != self.basic_number +1:
                self.x += 1
                self.save()
            self.basic_number += 1
            print(self.number)
        print(self.coordinates[1024])

    def save(self):
        # if not (self.x, self.y) in self.coordinates.values():
        self.coordinates[self.number] = (self.x, self.y)
        self.number += 1

    def result(self, number):
        a, b = self.coordinates[number]
        if a < 0:
            a = -a
        if b < 0:
            b = -b
        result = a + b
        return result

Solution = Solution()
Solution.algorithm()
print(Solution.result(312051))

