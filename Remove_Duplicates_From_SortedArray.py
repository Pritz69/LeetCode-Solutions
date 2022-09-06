class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = 0
        for i in range(len(nums)):
            if nums[s] != nums[i]:
                s += 1
                nums[s] = nums[i]
        return s + 1
