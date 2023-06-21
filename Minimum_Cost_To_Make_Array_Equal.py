class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        l=min(nums)
        r=max(nums)+1
        def costc(l) :
            t=0
            for i,v in enumerate(nums) :
                t += abs(l-v) * cost[i]
            return t
        while l<r :
            m=(l+r)//2
            if costc(m) < costc(m+1) :
                r=m
            else :
                l=m+1
        return costc(l)
