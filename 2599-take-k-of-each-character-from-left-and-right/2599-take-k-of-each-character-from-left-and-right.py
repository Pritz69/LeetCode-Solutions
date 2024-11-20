class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        limitMap = Counter(s)
        for ch in 'abc':
            if limitMap[ch] < k:
                return -1
            limitMap[ch] -= k
        
        currCntMap = defaultdict(int)
        res = 0
        l = 0
        for r in range(n):
            currCntMap[s[r]] += 1
            while currCntMap[s[r]] > limitMap[s[r]] :
                currCntMap[s[l]] -= 1
                l += 1
            res = max(res,r-l+1)
        return n - res
