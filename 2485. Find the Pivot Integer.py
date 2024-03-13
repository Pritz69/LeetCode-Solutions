class Solution:
    def pivotInteger(self, n: int) -> int:
        s=n*(n+1)//2
        p=int(sqrt(s))
        if p*p==s :
            return p
        return -1
