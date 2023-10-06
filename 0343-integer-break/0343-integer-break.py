class Solution:
    def integerBreak(self, n: int) -> int:
        if n==2 or n==3 :
            return n-1
        if n==4 :
            return 4
        res=1
        while n > 4 :
            n -=3
            res *= 3
        return n*res