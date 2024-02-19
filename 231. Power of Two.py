class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0 :
            return 0
        x=int((log2(n)))
        return n==2**x
