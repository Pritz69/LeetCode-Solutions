class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n&(n-1)==0 and (n-1)%3 == 0