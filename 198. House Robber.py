class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[0]*(n+1)
        dp[0]=0
        dp[1]=nums[0]
        for i in range(2,n+1) :
            dp[i]=max(dp[i-2]+nums[i-1],dp[i-1])
        print(dp)
        return dp[n]


class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        def rec(i) :
            if i in dp :
                return dp[i]
            if i>=n :
                return 0
            t=nums[i]+rec(i+2)
            nt=rec(i+1)
            dp[i]=max(t,nt)
            return dp[i]
        dp={}
        return rec(0)
