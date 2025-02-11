class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        n=len(part)
        part=list(part)
        st=[]
        for i,x in enumerate(s):
            if st[-n:]==part :
                st=st[:-n]
            st.append(x)
        if st[-n:]==part :
            st=st[:-n]
        return "".join(st)