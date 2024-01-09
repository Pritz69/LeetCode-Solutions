class Solution:
    def beautySum(self, s: str) -> int:
        sm = 0
        for i in range(len(s)):
            d = defaultdict(int)
            m, mi = float('-inf'), float('inf')
            for j in range(i, len(s)):
                d[s[j]] +=1
                values = list(d.values())
                max_freq = max(values)
                min_freq = min(values)
                sm += max_freq - min_freq
        return sm
