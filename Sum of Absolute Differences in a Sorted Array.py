class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        s=sum(nums)
        ls=0
        rs=0
        res=[]
        for i in range(len(nums)) :
            rs = s - ls - nums[i]
            vl = nums[i]*i - ls
            vr = rs - (nums[i]*(len(nums)-i-1))
            res.append(vl+vr)
            ls += nums[i]
        return res
