class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        co=0
        total=0
        for c in costs :
            if c >= coins:
                break
            total +=c 
            if total <= coins :
                co +=1
            else :
                break 
        return co
