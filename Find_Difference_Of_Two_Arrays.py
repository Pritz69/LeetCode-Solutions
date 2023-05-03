class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        d2=dict()
        for x in nums2 :
            if x in d2 :
                d2[x] +=1
            else :
                d2[x] =1
        d1=dict()
        for x in nums1 :
            if x in d1 :
                d1[x] +=1
            else :
                d1[x] =1
        l1=[]
        l2=[]
        for x in nums1 :
            if x not in d2 :
                l1.append(x)
        for x in nums2 :
            if x not in d1 :
                l2.append(x)
        ans=[]
        ans.append(set(l1))
        ans.append(set(l2))
        return ans

        
