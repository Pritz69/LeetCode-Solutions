class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[defaultdict(int)for _ in range(n)]
        output=0
        for i in range(n):
            for j in range(i):
                d=nums[i]-nums[j]
                dp[i][d] +=(1+dp[j][d])
                output +=dp[j][d]
        return output
