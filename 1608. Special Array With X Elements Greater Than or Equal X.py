class Solution:
    def specialArray(self, nums: List[int]) -> int:
        m = max(nums)
        d = defaultdict(int)
        for i in range(0, m + 1):
            c = 0
            for x in nums:
                if x >= i:
                    c += 1
            d[i] = c
        ans = -1
        for i in range(0, m + 1):
            if d[i] == i:
                ans = i
                break
        return ans


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        i = 0
        while i < len(nums) and nums[i] > i:
            i += 1
        return -1 if i < len(nums) and i == nums[i] else i
