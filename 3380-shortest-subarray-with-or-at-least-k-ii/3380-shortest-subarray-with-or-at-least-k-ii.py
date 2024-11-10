class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        def update_bit(num, rem):
            cur = 0
            for i in range(len(bits)):
                bits[~i] += ((num>>i)&1)*rem
                cur += (bits[~i] > 0)*(2**i)
            return cur
        
        
        ans = inf
        bits = [0]*32
        l = 0
        for r in range(len(nums)):
            cur = update_bit(nums[r], 1)
            while cur >= k and l <= r:
                ans = min(ans, r-l+1)
                cur = update_bit(nums[l], -1)
                l += 1
        return ans if ans != inf else -1