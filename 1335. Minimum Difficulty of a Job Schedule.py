class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        if len(jobDifficulty) == d:
            return sum(jobDifficulty)

        def rec(i, k, m):
            if (i, k, m) in dp:
                return dp[(i, k, m)]

            if i == len(jobDifficulty):
                if k == d:
                    return 0
                else:
                    return float('inf')  
            if k==d :
                return float("inf")
            m = max(m, jobDifficulty[i])
            t = m + rec(i + 1, k + 1, -1)
            nt = rec(i + 1, k, m)
            c = min(t, nt)
            dp[(i, k, m)] = c
            return c

        dp = {}
        return rec(0, 0, 0)
