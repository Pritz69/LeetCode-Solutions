class Solution:
    def shortestPalindrome(self, s: str) -> str:
        pr=0
        su=0
        b=29
        li=0
        p=1
        mod=10**9 + 7
        for i,c in enumerate(s) :
            ch=(ord(c)-ord('a')+1)
            pr=(pr*b)%mod
            pr=(pr+ch)%mod
            su=(su+ch*p)%mod
            p=(p*b)%mod
            if pr==su :
                li=i
        su=s[li+1:]
        return su[::-1]+s