class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        c=0
        s,m=neededTime[0],neededTime[0]
        for i in range(1,len(colors)) :
            if colors[i]==colors[i-1] :
                s += neededTime[i]
                m=max(m,neededTime[i])
            else :
                c += s-m
                s,m=neededTime[i],neededTime[i]
        c += s-m
        return c
