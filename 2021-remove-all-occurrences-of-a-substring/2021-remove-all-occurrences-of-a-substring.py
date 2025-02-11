class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        n=len(part)
        st=[]
        for i,x in enumerate(s):
            if "".join(st[-n:])==part :
                st=st[:-n]
            st.append(x)
        if "".join(st[-n:])==part :
            st=st[:-n]
        return "".join(st)