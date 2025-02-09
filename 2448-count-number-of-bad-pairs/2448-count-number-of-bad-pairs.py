class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        tot = len(nums) * (len(nums) - 1) // 2
        good = 0
        dp = {}
        
        for i,num in enumerate(nums):
            v = i - num
            good += dp.get(v, 0)
            dp[v] = dp.get(v, 0) + 1
        
        return tot - good