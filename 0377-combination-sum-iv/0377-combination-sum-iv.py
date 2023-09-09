class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp=[-1]*(target+1)
        dp[0]=1
        def rec(nums,target,dp) :
            if dp[target] != -1 :
                return dp[target]
            res=0
            for n in nums :
                if n <=target :
                    res += rec(nums,target-n,dp)
            dp[target]=res
            return res
        rec(nums,target,dp)
        return dp[target]
    
