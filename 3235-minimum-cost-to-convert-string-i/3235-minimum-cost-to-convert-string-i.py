class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n = len(original)
        d = [[float('inf')] * 26 for _ in range(26)]
        for i in range(n):
            src = ord(original[i]) - 97
            dst = ord(changed[i]) - 97
            wt = cost[i]
            d[src][dst] = min(d[src][dst], wt)
        for i in range(26):
            d[i][i] = 0
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])
        ans = 0
        for i in range(len(source)):
            src = ord(source[i]) - 97
            dst = ord(target[i]) - 97
            if d[src][dst] == float('inf'):
                return -1
            ans += d[src][dst]
        return ans