class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n=len(nums)
        dp={}
        for i in range(n) :
            for j in range(i+1,n) :
                diff=nums[j]-nums[i]
                dp[(j,diff)] = dp.get((i,diff) , 1) + 1
        return max(dp.values())
