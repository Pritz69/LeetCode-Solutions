class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost) :
            return -1
        t=0
        r=0
        for i in range(len(gas)):
            t += gas[i]-cost[i]
            if t < 0 :
                t =0
                r =i+1
        return r
