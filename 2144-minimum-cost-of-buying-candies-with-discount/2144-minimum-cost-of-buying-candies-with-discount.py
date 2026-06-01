class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        if len(cost)==1 :
            return cost[0]
        if len(cost)==2 :
            return cost[0] + cost[1]
        cost=sorted(cost,reverse=True)
        print(cost)
        ans=0
        i=2
        while i < len(cost) :
            if min(cost[i-2],cost[i-1]) >= cost[i] :
                ans = ans + cost[i-2] + cost[i-1]
            else :
                ans = ans + cost[i-2] + cost[i-1] + cost[i]
            i +=3
            #print(ans)
        if len(cost)%3==0 :
            return ans
        elif len(cost)%3==1 :
            return ans+cost[-1]
        elif len(cost)%3==2 :
            return ans+cost[-1]+cost[-2]