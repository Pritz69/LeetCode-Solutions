class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n=len(weights)
        pairs=[0]*(n-1)
        for r in range(n-1) :
            pairs[r]=weights[r] + weights[r+1]
        pairs.sort()
        ans=0
        for r in range(k-1) :
            ans += pairs[n-2-r] - pairs[r]
        return ans
