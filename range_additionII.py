class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        mnr,mnc=m,n
        for r,c in ops:
            mnr,mnc=min(mnr,r),min(mnc,c)
        return mnr*mnc
