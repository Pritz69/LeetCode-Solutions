class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        l,m=0,0
        c=defaultdict(int)
        res=0
        for r in range(len(nums)) :
            c[nums[r]] +=1
            while len(c) > k :
                c[nums[m]] -=1
                if c[nums[m]]==0 :
                    c.pop(nums[m])
                m +=1
                l=m
            while c[nums[m]] > 1 :
                c[nums[m]]-=1
                m +=1 
            if len(c)==k :
                res += (m-l)+1
        return res