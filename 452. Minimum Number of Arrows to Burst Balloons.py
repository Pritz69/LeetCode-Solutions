class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        #print(points)
        pos=points[0][1];
        c=1
        for i in range(1,len(points)) :
            if pos >= points[i][0] :
                continue
            c +=1
            pos=points[i][1]
        return c
