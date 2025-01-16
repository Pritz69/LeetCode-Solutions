class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        a=0
        for x in nums1 :
            a=a^x
        b=0
        for x in nums2 :
            b=b^x
        ans=0
        if len(nums1)%2==0 and len(nums2)%2==0:
            ans=0
        elif len(nums1)%2==1 and len(nums2)%2==1 :
            ans=a^b
        elif len(nums2)%2==0 :
            ans=b
        elif len(nums1)%2==0 :
            ans=a
        return ans