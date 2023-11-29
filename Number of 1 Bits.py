class Solution:
    def hammingWeight(self, n: int) -> int:
        c=0
        while n>0 :
            if n&1 :
                c +=1
            #print(n)
            n = n>>1
        return c
