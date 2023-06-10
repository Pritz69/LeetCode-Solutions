class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def getsum(v) :
            c = 0
            if v > index :
                c += (v + v - index) * (index+1) // 2
            else :
                c += (v + 1) * v // 2 + index - v + 1
            if v >= n - index :
                c += (v + v - n + 1 + index) * (n - index) // 2
            else :
                c += (v + 1) * v // 2 + n - index - v 
            return c - v
        l,r=1,maxSum
        while l < r :
            m = (l+r+1)//2
            if getsum(m) <= maxSum :
                l = m
            else :
                r = m - 1
        return l 
