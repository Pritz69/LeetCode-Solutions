class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        x=0
        for c in nums :
            x=x^c
        #100
        if x==k :
            return 0
        ans=x^k
        #100 ^ 001 == > 101
        #a^b=c then a^c=b
        c=0
        while ans :
            if ans&1  :
                c +=1
            ans = ans >> 1
        #counting the no of 1's in 101 
        #comm and assoc prop of xor
        return c
