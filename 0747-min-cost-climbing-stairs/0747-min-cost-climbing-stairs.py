class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp={}
        def rec(i) :
            if i>=len(cost) :
                return 0
            if i in dp :
                return dp[i]
            tk1 = cost[i] + rec(i+1)
            tk2 = cost[i] + rec(i+2)
            dp[i] = min(tk1,tk2)

            return dp[i]
        
        return min(rec(0),rec(1))