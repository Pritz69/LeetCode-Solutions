class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        d=dict()
        for i in nums1 :
            if i not in d :
                d[i]=1
            else :
                d[i] +=1 
        for i in nums2 :
            if i in d:
                return i 
        return -1
        
