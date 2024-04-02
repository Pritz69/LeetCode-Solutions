class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = defaultdict(str)
        d2 = defaultdict(str)
        for i in range(len(s)):
            if s[i] in d:
                if d[s[i]] != t[i]:
                    return False
            if t[i] in d2:
                if d2[t[i]] != s[i]:
                    return False
            d[s[i]] = t[i]
            d2[t[i]] = s[i]
        return True
