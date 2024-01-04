class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        def rec(i):
            if i == 0:
                return 0
            if i < 0:
                return 10**7
            if i in dp:
                return dp[i]
            c = 0  
            t3 = c + 1 + rec(i - 3)
            t2 = c + 1 + rec(i - 2)
            dp[i] = min(t3, t2)
            return dp[i]
        dp = {}
        ans = 0
        f=0
        for x in cnt:
            v=rec(cnt[x])
            if v>10**6 :
                f=1
            else :
                ans +=v
        return -1 if f==1 else ans


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        ans = 0
        for c in counter.values():
            if c == 1: 
                return -1
            ans += ceil(c / 3)
        return ans
