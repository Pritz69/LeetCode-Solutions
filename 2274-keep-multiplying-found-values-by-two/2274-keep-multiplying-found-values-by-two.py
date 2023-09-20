class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        d={}
        for x in nums :
            d[x]=d.get(x,0)+1
        ans=original
        while ans in d :
            ans=ans*2
        return ans