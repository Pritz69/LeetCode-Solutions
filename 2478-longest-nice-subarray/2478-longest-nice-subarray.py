class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        # Binary search for the longest nice subarray length
        left, right = 0, len(nums)
        result = (1)

        while left <= right:
            length = left + (right - left) // 2
            if self._can_form_nice_subarray(length, nums):
                result = length  
                left = length + 1 
            else:
                right = length - 1  

        return result
    def _can_form_nice_subarray(self, length: int, nums: list[int]) -> bool:
        if length <= 1:
            return True  

        for start in range(len(nums) - length + 1):
            bit_mask = 0  
            is_nice = True

            for pos in range(start, start + length):
                
                if bit_mask & nums[pos] != 0:
                    is_nice = False
                    break
                bit_mask |= nums[pos]  

            if is_nice:
                return True

        return False 