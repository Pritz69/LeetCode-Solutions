class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        s=0
        t=0
        for x in bills :
            if x==5 :
                s +=1
            if x==10 :
                if s >= 1 :
                    s -=1
                    t +=1
                else :
                    return False
            if x==20 :
                if t >=1 and s>=1 :
                    t -=1
                    s -=1
                elif s >= 3 :
                    s -=3
                else :
                    return False
        return True 