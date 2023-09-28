class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n=len(points)
        m=float('-inf')
        for i in range(n) :
          for j in range(n) :
            for k in range(n) :
                m=max(m, 0.5*abs( points[i][0]*(points[j][1]-points[k][1]) + points[j][0]*(points[k][1]-points[i][1]) + points[k][0]*(points[i][1]-points[j][1]) ) ) 
        return m

        	 
  #  Ax * (	 B	y 	−	 C	y 	) 	+	 Bx * (	 C	y 	−	 A	y 	) 	+	 Cx * (	 A	y 	−	 B	y 	)  / 2