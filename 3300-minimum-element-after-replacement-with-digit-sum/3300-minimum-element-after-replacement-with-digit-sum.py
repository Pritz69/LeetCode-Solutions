class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans=float('inf')
        for n in nums :
            s=0
            while n :
                s=s+(n%10)
                n=n//10
            ans=min(ans,s)
        return ans