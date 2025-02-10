class Solution:
    def clearDigits(self, s: str) -> str:
        st=[]
        for x in s :
            if x in "0123456789" :
                st.pop()
            else :
                st.append(x)
        return "".join(st) 