class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s=0
        l=[]
        for i in nums :
            s +=i
            l.append(s)
        return l
