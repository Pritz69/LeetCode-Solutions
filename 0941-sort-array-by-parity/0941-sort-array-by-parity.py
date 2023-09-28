class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l=0
        r=0
        while l<len(nums) and r<len(nums) :
            if nums[r]&1==1 :
                #l=r
                while l<len(nums) and nums[l]&1==1 :
                    l +=1
                if l < len(nums):
                    t=nums[l]
                    nums[l]=nums[r]
                    nums[r]=t
            else :
                l=r+1
            r +=1
        return nums