# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList):
        self.flattenlist = []
        self.c = 0
        for x in nestedList:
            self.flatten(x)

    def next(self):
        result = self.flattenlist[self.c]
        self.c += 1
        return result

    def hasNext(self):
        return self.c < len(self.flattenlist)

    def flatten(self, x):
        if x.isInteger():
            self.flattenlist.append(x.getInteger())
        else:
            for y in x.getList():
                self.flatten(y)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())