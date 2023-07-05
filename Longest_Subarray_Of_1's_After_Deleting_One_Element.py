class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l=0
        r=0
        c=0
        ans=0
        prev=0
        while r<len(nums) :
            if nums[r]==0 :
                c +=1
                if c>1 :
                    l=prev+1
                    c-=1
                prev=r
            if c<=1 :
                ans=max(ans,r-l)
            r +=1
        return ans

     

      
