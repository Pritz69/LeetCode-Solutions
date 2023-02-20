class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        mid = (hi + lo) // 2
        while lo <= hi:
            mid = (hi + lo) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1   
            else:
                hi = mid - 1   
        if(nums[mid]<target):
            return mid+1
        return mid
