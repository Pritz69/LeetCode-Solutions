class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0 :
            return 0
        if n<=2 :
            return 1
        a,b,c=0,1,1
        for i in range(n-2) :
            s=a+b+c
            a=b
            b=c
            c=s
        return s
