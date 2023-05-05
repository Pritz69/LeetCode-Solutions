class Solution:
    def largestOddNumber(self, num: str) -> str:
        i=-1
        for x in range(len(num)-1,-1,-1) :
            if int(num[x])%2 == 1 :
                i=x
                break
        return num[:i+1]
