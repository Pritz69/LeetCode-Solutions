class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        res=[0]*n
        st=[]
        for i,t in enumerate(temperatures):
            while st and t >st[-1][0] :
                stt,sti=st.pop()
                res[sti]=(i-sti)      
            st.append([t,i])
        return res
