class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l,r=0,int(c**0.5)
        while l <= r:
            ans=l*l + r*r
            if ans  < c :
                l +=1
            elif ans > c :
                r -=1
            else :
                return True
        return False 