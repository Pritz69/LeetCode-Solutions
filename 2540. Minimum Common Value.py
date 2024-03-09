class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        s2=set()
        for x in nums2 :
            s2.add(x)
        for x in nums1 :
            if x in s2 :
                return x
        return -1
