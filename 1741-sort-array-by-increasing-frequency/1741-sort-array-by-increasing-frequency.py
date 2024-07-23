class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        c=Counter(nums)
        c=sorted(c.items(),key=lambda x:(x[1],-x[0]))
        ans=[]
        for x in c :
            ans +=[x[0] for i in range(x[1])]
        return ans