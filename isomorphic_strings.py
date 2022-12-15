class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        for i, n in enumerate(s):
            if n not in d: d[n]=t[i]
            else:
                if d[n] != t[i]:
                    return False
        return len(d.keys()) == len(set(d.values()))
