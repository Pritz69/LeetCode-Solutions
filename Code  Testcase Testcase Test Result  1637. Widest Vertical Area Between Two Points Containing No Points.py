class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        m=0
        for i in range(len(points)-1) :
            m=max(m,points[i+1][0]-points[i][0])
        return m
