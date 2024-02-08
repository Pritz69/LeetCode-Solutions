class Solution:
    def myAtoi(self, s: str) -> int:
        if not s :
            return 0
        while s[0]==" " :
            s=s[1:]
            if not s :
                return 0
        x,f,sf=0,0,0
        sign=""
        for c in s :
            if c in "+-" :
                if sf==1 or f==1:
                    break
                sign=c
                f=1
            elif c in "0123456789" :
                x = x*10 + int(c)
                sf=1
            else :
                break
        if sign=='-' :
            x=max(-x,-2147483648)
            return x
        else :
            x=min(x,2147483647)
            return x
