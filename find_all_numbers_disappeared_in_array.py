class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums :
            i=abs(n)-1
            nums[i]=-1 *(abs(nums[i]))
        res=[]
        for i,n in enumerate(nums):
            if n>0 :
                res.append(i+1)
        return res
      
      
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        missing = []
        s = set(nums)
        n = len(nums)
        for i in range(1,n+1):
            if i not in s:
                missing.append(i)
        return missing
