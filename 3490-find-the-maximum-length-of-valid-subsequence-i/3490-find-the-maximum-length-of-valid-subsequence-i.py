class Solution(object):
    def maximumLength(self, nums):
        c = nums[0] % 2
        odd = even = both = 0
        for num in nums:
            if num % 2 == 0:
                even += 1
            else:
                odd += 1
            if num % 2 == c:
                both += 1
                c = 1 - c  # Toggle the parity
        return max(both, even, odd)
        