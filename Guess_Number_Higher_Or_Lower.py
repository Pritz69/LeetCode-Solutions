# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        s = 1
        e = n+1
        while s+1<e:
            mid = (s+e)//2
            if guess(mid)>=0:
                s = mid
            else:
                e = mid
        return s
                
