class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)) :
            v=abs(nums[i])
            if nums[v-1] < 0 :
                ans.append(v)
            nums[v-1]=-nums[v-1]
        return ans
