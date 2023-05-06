class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        ans=0
        nums.sort()
        i,j=0,len(nums)-1
        while(i<=j):
            if nums[i]+nums[j]<=target:
                ans+=pow(2,(j-i),1000000007)
                i+=1
            else:
                j-=1
        return ans%1000000007
