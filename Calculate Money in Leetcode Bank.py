class Solution:
    def totalMoney(self, n: int) -> int:
        if n <= 7 :
            return (n*(n+1))//2
        s=0
        v=28
        c=0
        l=7
        while n >= 7 :
            s +=v
            c +=1
            l +=1
            v -=c
            v +=l
            n -=7
        c +=1
        while n > 0 :
            s += c
            c += 1
            n -= 1
        return s
        
