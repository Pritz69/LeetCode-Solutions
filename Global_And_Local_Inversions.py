class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        for r in range(len(nums)) :
            if abs(nums[r]-r) > 1 :
                return False
        return True
