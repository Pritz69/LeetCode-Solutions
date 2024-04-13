class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        ls=[0]*n
        rs=[0]*n
        st=[]
        for i in range(n) :
            while st and heights[st[-1]] >= heights[i] :
                st.pop()
            if not st :
                ls[i]=0
            else :
                ls[i]=st[-1] + 1
            st.append(i)
        st=[]
        for i in range(n-1,-1,-1) :
            while st and heights[st[-1]] >= heights[i] :
                st.pop()
            if not st :
                rs[i]=n-1
            else :
                rs[i]=st[-1] - 1
            st.append(i)
        m=0
        for i in range(n) :
            m=max(m,heights[i]*(rs[i]-ls[i]+1))
        return m



class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        st=[]
        m=0
        for i in range(n+1) :
            while st and (i==n or heights[st[-1]] >= heights[i]) :
                h=heights[st.pop()]
                w=0
                if not st :
                    w=i
                else :
                    w=i-st[-1]-1
                m=max(m,h*w)
            st.append(i)
        return m
