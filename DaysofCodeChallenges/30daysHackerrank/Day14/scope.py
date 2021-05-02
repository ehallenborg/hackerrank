class Difference:
    def __init__(self, a):
        self.__elements = a
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        maxval = 0
        for i in self.__elements:
            for j in self.__elements:
                diff = abs(i - j)
                maxval = max(diff, maxval)
    
        self.maximumDifference = maxval
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)