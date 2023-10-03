class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c=0
        d={}
        for x in nums :
            d[x]=d.get(x,0) + 1
        for x in d :
            c += (d[x] * (d[x]-1))//2
        return c