class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        N=len(nums)
        product=1
        subarray=0
        total=0
        mini=0
        for i in range(N):
            product *=nums[i]
            subarray +=1
            while product >= k and mini<=i:
                product /= nums[mini]
                mini +=1
                subarray -=1
            if product < k:
                total +=subarray 
        return total
