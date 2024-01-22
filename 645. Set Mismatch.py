class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        c=Counter(nums)
        ans=[]
        for i in range(1,len(nums)+1) :
            if c[i]==2 :
                ans.append(i)
        for i in range(1,len(nums)+1) :
            if i not in c :
                ans.append(i)
        return ans
