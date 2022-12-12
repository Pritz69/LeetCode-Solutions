class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num==0:
            return True
        num=str(num)
        s1=num.strip('0')
        s1=s1[::-1]
        s2=s1[::-1]
        if s2==num :
            return True
        else :
            return False
