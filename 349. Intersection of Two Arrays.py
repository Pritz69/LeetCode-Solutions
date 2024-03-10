class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s=set(nums2)
        ans=set()
        for x in nums1 :
            if x in s :
                ans.add(x)
        return ans
