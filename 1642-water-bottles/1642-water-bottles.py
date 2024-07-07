class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans=numBottles
        while numBottles >= numExchange  :
            c=numBottles//numExchange
            r=numBottles%numExchange
            ans += c
            numBottles=c+r
        return ans