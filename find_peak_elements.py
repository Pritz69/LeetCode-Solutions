class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        if len(nums) == 1:
            return 0
        
        while right > left:
            mid = (left + right)//2
            
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            
            if nums[mid] < nums[mid+1]:
                left = mid + 1
                
            else:
                right = mid - 1
        
        return  right if nums[right] > nums[mid] else mid
