class Solution:
    def longestObstacleCourseAtEachPosition(self, nums: List[int]) -> List[int]:
        res=[]
        dp=[10**8]*(len(nums)+1)
        for n in nums :
            ind = bisect.bisect(dp,n)
            res.append(ind+1)
            dp[ind]=n
        return res

# res = [1233]
# dp = [12299]
