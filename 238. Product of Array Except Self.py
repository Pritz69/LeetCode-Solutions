class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ps=[1]*(len(nums))
        ps[0]=nums[0]
        for i in range(1,len(nums)) :
            ps[i]=ps[i-1]*nums[i]
        ss=[1]*(len(nums))
        ss[len(nums)-1]=nums[len(nums)-1]
        for i in range(len(nums)-2,-1,-1) :
            ss[i]=ss[i+1]*nums[i]
        ans=[1]*len(nums)
        ans[0]=ss[1]
        ans[len(nums)-1]=ps[len(nums)-2]
        for i in range(1,len(nums)-1) :
            ans[i]=ps[i-1]*ss[i+1]
        return ans
