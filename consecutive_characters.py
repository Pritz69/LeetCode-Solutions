class Solution:
    def maxPower(self, s: str) -> int:
        c = 0
        mc = 0
        p = None
        for x in s:
            if x == p:
                c += 1
            else:
                p = x
                c = 1
            mc = max(mc, c)
        return mc
