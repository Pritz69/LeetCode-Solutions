class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        c=0
        s=0
        m=0
        f=0
        for i in range(len(nums)) :
            if c>=2 and s > nums[i] :
                m=max(m,s+nums[i])
                f=1
            s += nums[i]
            c += 1    
        if f==0 :
            return -1
        return m
