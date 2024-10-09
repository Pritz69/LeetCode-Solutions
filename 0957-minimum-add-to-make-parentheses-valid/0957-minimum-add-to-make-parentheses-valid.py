class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st=[]
        c=0
        for x in s :
            if st and x==")" :
                st.pop()
            elif x=="(" :
                st.append(x)
            else :
                c +=1
        return len(st)+c