class Solution:
    def titleToNumber(self, n: str) -> int:
        ans=0
        for x in n :
           ans = ans*26 + (ord(x)-64)
        return ans