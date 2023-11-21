class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        d={}
        for x in nums :
            s = str(x)
            s = s[::-1]
            s = int(s)
            v = x - s
            d[v] = d.get(v,0) + 1
        ans=0
        for x in d :
            v = d[x]
            ans = (ans + (v * (v - 1) // 2)) % 1000000007
        return ans
