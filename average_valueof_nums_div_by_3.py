class Solution:
    def averageValue(self, nums: List[int]) -> int:
        s=0
        c=0
        for i in nums :
            if i%2==0 and i%3==0 :
                c +=1
                s +=i
        if c==0:
            return 0
        else :
            return s//c
