class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m=float('-inf')
        sm=float('-inf')
        for x in nums :
            if x>m :
                sm=m
                m=x
            elif x>sm :
                sm=x
        #print(m,sm)
        return (m-1)*(sm-1)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a,b=heapq.nlargest(2,nums)
        return (a-1)*(b-1)
