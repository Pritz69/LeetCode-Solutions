class Solution:
    def check(self, nums: List[int]) -> bool:
        l=len(nums)
        na=[]
        for i in range(1,l) :
            if nums[i-1] > nums[i] :
                na=nums[i:] + nums[:i]
        #print(na)
        for i in range(1,len(na)) :
            if na[i-1] > na[i] :
                return False
        return True