class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        s=set(nums)
        m=max(nums)
        ans=-1
        for x in nums :
            c=0
            n=x
            while n <=m and n in s : 
                n=n**2
                c +=1
            ans=max(ans,c)
        return -1 if ans==1 else ans
            