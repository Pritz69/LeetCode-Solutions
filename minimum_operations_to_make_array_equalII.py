class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k==0 :
            for i in range(len(nums1)) :
                if nums1[i] != nums2[i] :
                    return -1
            return 0 
        if k > 0 :
            add=0
            sub=0
            diff=0
            for i in range(len(nums1)) :
                diff = nums1[i]-nums2[i] 
                if diff%k !=0  :
                    return -1
                if diff > 0 :
                    sub += diff//k 
                if diff < 0 :
                    add += abs(diff//k)
            if add==sub :
                return add
            return -1
