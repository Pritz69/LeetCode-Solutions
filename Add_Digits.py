class Solution:
    def addDigits(self, num: int) -> int:
        while (len(str(num))>1) :
            s=sum(int(x) for x in str(num))
            num=int(s)
        return num
