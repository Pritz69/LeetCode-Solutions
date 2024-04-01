class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans=numBottles
        ex=0
        while numBottles >= numExchange :
            numBottles -=numExchange
            numExchange +=1
            ex +=1
            if numBottles <= numExchange :
                numBottles +=ex
                ans += ex
                ex=0
        return ans
