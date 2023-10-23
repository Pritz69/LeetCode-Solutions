class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n&(n-1)==0 and (n-1)%3 == 0

        # n&(n-1) filters out all the powers of 2, now not all powers of 2 are powers of 4, but the alternate ones, more precisely the one which have multiple of 3 before it, example 16,64 and not 8 and 32.   