class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def func(histo) :
            area=0
            st=[]
            n=len(histo)
            for i in range(n+1) :
                while st and (i==n or histo[st[-1]]>=histo[i]) :
                    h=histo[st.pop()]
                    w=0
                    if not st :
                        w=i
                    else :
                        w=i-st[-1]-1
                    area=max(area,h*w)
                st.append(i)
            return area

        n=len(matrix)
        m=len(matrix[0])
        histo=[0]*m
        ans=0
        for i in range(n) :
            for j in range(m) :
                if matrix[i][j]=='1' :
                    histo[j] =histo[j]+1
                else :
                    histo[j] = 0
            ans=max(ans,func(histo))
        return ans
