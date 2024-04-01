class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s=0
        n=x
        while x :
            s += x%10
            x=x//10
        if n%s==0 :
            return s
        else :
            return -1
