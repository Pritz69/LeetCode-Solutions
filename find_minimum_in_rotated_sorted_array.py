class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left+right) // 2
            if nums[mid+1] < nums[mid]:
                return nums[mid+1]
	    # left sorted
            if nums[mid] > nums[left]:
	    # search on right
                left = mid + 1
	    # right sorted
            else:
		  # search on left
                right = right - 1
        return nums[0]
