from sortedcontainers import SortedDict
class SummaryRanges:

    def __init__(self):
        self.treeMap = SortedDict()

    def addNum(self, value: int) -> None:
        self.treeMap[value] = True

    def getIntervals(self) -> List[List[int]]:
        res=[]
        for n in self.treeMap :
            if res and res[-1][1] + 1 == n :
                res[-1][1]=n
            else :
                res.append([n,n])
        return res
