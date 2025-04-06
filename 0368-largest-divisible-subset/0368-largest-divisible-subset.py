class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n=len(nums)
        m=0
        dp=[0]*(n)
        h=[0]*(n)
        lind=0
        for i in range(n) :
            dp[i]=1
            h[i]=i
            for j in range(i) :
                if nums[i] % nums[j] == 0 and dp[j]+1 >dp[i]:
                    dp[i]=dp[j]+1
                    h[i]=j
            if dp[i] > m :
                m=dp[i]
                lind=i
        ans=[]
        #print(lind,h)
        while(h[lind]!=lind) :
            ans.append(nums[lind])
            lind=h[lind]
        ans.append(nums[lind])
        return ans[::-1]