class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        s=[]
        for i in nums :
            for x in str(i) :
                s.append(int(x))
        return s
