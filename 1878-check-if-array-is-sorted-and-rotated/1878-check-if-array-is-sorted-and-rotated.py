class Solution:
    def check(self, nums: List[int]) -> bool:
        n=len(nums)
        for i in range(n) :
            ans=nums[i:]+nums[:i]
            f=0
            for i in range(1,len(ans)) :
                if ans[i-1] > ans[i] :
                    f=1
            if f==0 :
                return True
        return False