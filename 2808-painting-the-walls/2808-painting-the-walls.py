class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        def rec(i,remain) :
            if remain <= 0 :
                return 0
            if i==len(cost) :
                return float('inf')
            if (i,remain) in dp :
                return dp[(i,remain)]
            paint = cost[i] + rec(i+1,remain-1-time[i])
            skip = rec(i+1,remain)

            dp[(i,remain)] = min(paint,skip)
            return dp[(i,remain)]
        dp={}
        return rec(0,len(cost))