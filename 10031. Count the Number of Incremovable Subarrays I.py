class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        ans=0
        n=len(nums)
        for i in range(n) :
            for j in range(i,n) :
                f=0
                l=-1
                for k in range(i) :
                    if nums[k] <= l :
                        f=1
                        break
                    l=nums[k]
                for k in range(j+1,n) :
                    if nums[k] <= l :
                        f=1
                        break
                    l=nums[k]
                if f==0 :
                    ans +=1
        return ans
