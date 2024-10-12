class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        st,ed=[],[]
        for l,r in intervals :
            st.append(l)
            ed.append(r)
        st.sort()
        ed.sort()
        grp=0
        res=0
        i=0
        j=0
        while i < len(st) :
            if st[i] <= ed[j] :
                i +=1
                grp +=1
            else :
                j +=1
                grp -=1
            res=max(res,grp)
        return res