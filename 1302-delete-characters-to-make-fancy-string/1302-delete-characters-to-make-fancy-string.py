class Solution:
    def makeFancyString(self, s: str) -> str:
        st=[]
        for x in s :
            if len(st) >=2 and st[-1]==st[-2]==x :
                continue
            else :
                st.append(x)
        ans=""
        for x in st :
            ans +=x
        return ans