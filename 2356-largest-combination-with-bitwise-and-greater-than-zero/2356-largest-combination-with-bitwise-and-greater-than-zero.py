class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        mx=0
        n=int(log2(max(candidates)))
        for i in range(n+1) :
            c=0
            for x in candidates :
                if x & (1 << i) :
                    c=c+1
            mx=max(mx,c)
        return mx
            