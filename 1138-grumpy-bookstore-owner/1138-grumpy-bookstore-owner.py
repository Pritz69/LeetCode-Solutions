class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        take=0
        l=0
        maxsm=0
        sm=0
        for r in range(len(customers)) :
            if grumpy[r]==1 :
                sm += customers[r]
            else :
                take += customers[r]
            if r-l + 1 > minutes :
                if grumpy[l]==1 :
                    sm -= customers[l]
                l +=1
            maxsm=max(maxsm,sm)
        return maxsm+take