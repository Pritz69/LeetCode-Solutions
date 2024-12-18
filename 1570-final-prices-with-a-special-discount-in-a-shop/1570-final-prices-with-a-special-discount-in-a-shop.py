class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices)) :
            v=0
            for j in range(i+1,len(prices)) :
                if prices[j] <= prices[i] :
                    v=prices[j]
                    break
            prices[i] -= v
        return prices