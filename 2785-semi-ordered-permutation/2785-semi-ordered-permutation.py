class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n=len(nums)
        if nums[0]==1 and nums[n-1]==n :
            return 0
        c=0
        for i in range(n) :
            if nums[i]==1 and i==0 :
                break
            if nums[i]==1 :
                while nums[0] !=1 :
                    t=nums[i-1]
                    nums[i-1]=nums[i]
                    nums[i]=t
                    c +=1
                    i -=1
                break
        for i in range(n) :
            if nums[i]==n and i==n-1 :
                break
            if nums[i]==n :
                while nums[n-1] !=n :
                    t=nums[i+1]
                    nums[i+1]=nums[i]
                    nums[i]=t
                    c +=1
                    i +=1
                break
        return c
       