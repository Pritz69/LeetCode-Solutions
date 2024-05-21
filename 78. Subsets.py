class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=[]
        def rec(i,l) :
            if i==n :
                ans.append(l)
                return
            rec(i+1,l+[nums[i]])
            rec(i+1,l)
        rec(0,[])
