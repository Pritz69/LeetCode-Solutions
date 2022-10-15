class Solution:
    def isHappy(self, n: int) -> bool:
        v=set()
        while n not in v :
            v.add(n)
            n=self.sumofsqaures(n)
            if n==1 :
                return True
        return False
    def sumofsqaures(self,n:int)->int:
        o=0
        while n:
            d=n%10
            o+=d**2
            n=n//10
        return o
