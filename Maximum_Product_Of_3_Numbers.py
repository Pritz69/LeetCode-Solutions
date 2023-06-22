class Solution:
    def maximumProduct(self, l: List[int]) -> int:
        l.sort()
        return max(l[-1]*l[-2]*l[-3],l[0]*l[1]*l[-1])
