class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        d=[]
        for c1,c2 in costs:
            d.append([c2-c1,c1,c2])
        d.sort()
        res=0
        for i in range(len(costs)):
            if i <len(costs)//2:
                res +=d[i][2]
            else:
                res +=d[i][1]
        return res
