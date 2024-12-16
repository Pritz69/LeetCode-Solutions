class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        while k :
            mi=0
            mv=float('inf')
            for i,x in enumerate(nums) :
                if x < mv :
                    mv=x
                    mi=i
            nums[mi]=nums[mi]*multiplier
            k -=1
        return nums