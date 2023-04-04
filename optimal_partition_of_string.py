class Solution:
    def partitionString(self, s: str) -> int:
        se=set()
        res=1
        for c in s :
            if c in se :
                res +=1
                se=set()
            se.add(c)
        return res
