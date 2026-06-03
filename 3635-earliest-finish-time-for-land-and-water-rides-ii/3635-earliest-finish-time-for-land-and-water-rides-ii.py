class Solution:
    def solve(self, x, xd, y, yd):
        mn = float('inf')
        for i in range(len(x)):
            mn = min(mn, x[i] + xd[i])
        ans = float('inf')
        for i in range(len(y)):
            start_time = max(mn, y[i])
            ans = min(ans, start_time + yd[i])
        return ans

    def earliestFinishTime(self,
                           landStartTime,
                           landDuration,
                           waterStartTime,
                           waterDuration):

        land_first = self.solve(
            landStartTime,
            landDuration,
            waterStartTime,
            waterDuration
        )

        water_first = self.solve(
            waterStartTime,
            waterDuration,
            landStartTime,
            landDuration
        )

        return min(land_first, water_first)