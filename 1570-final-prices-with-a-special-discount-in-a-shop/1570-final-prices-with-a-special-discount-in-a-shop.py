class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        d={}
        for i,x in enumerate(prices) :
            d[i]=d.get(i,0)+x
        for i in range(len(prices)) :
            v=0
            ind=i+1
            while ind in d and d[ind] > prices[i] :
                ind +=1
            if ind in d :
                v=d[ind]
            prices[i]=prices[i]-v
        return prices