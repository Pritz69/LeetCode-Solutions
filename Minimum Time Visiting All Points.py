class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans=0
        for i in range(1,len(points)) :
            x=abs(points[i-1][0]-points[i][0])
            y=abs(points[i-1][1]-points[i][1])
            ans += max(x,y)
        return ans
