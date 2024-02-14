class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p,n=[],[]
        ans=[]
        for i,x in enumerate(nums) :
            if x>=0 :
                p.append(i)
            else :
                n.append(i)
        for j in range(len(p)) :
            ans.append(nums[p[j]])
            ans.append(nums[n[j]])
        return ans
