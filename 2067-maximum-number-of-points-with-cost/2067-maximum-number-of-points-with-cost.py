class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        R,C=len(points),len(points[0])
        row=points[0]
        for r in range(1,R) :
            nr=points[r].copy()
            left,right=[0]*C,[0]*C
            left[0]=row[0]
            for c in range(1,C) :
                left[c]=max(left[c-1]-1,row[c])
            right[C-1]=row[C-1]
            for c in range(C-2,-1,-1) :
                right[c]=max(right[c+1]-1,row[c])
            for c in range(C) :
                nr[c] += max(left[c],right[c])
            row=nr
        return max(row)