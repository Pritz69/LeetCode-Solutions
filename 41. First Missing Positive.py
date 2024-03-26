class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        f=0
        for x in nums :
            if x==1 :
                f=1
        if f==1 :
            n=len(nums)
            for i in range(n) :
                if nums[i] <= 0 or nums[i] > n : 
                    nums[i]=1
            for i in range(n) :
                ind=abs(nums[i])-1
                nums[ind]=-abs(nums[ind])
            for i in range(n) :
                if nums[i] > 0 :
                    return i+1
            return n+1
        else :
            return 1
