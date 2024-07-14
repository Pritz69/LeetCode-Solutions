class Solution:
    def countOfAtoms(self, formula: str) -> str:
        st=[defaultdict(int)]
        i=0
        while i < len(formula) :
            if formula[i]=="(" :
                st.append(defaultdict(int))
            elif formula[i]==")" :
                curmap=st.pop()
                cnt=""
                while i+1 <len(formula) and formula[i+1].isdigit():
                    cnt += formula[i+1]
                    i +=1
                cnt=1 if not cnt else int(cnt)
                prevmap=st[-1]
                for x in curmap :
                    prevmap[x] += curmap[x] * cnt
            else :
                el=formula[i]
                cnt=""
                if i+1 < len(formula) and formula[i+1].islower():
                    el=formula[i:i+2]
                    i +=1
                while i+1 <len(formula) and formula[i+1].isdigit():
                    cnt += formula[i+1]
                    i +=1
                cnt=1 if not cnt else int(cnt)
                curmap=st[-1]
                curmap[el] += cnt
            i +=1
        curmap=st[-1]
        ans=""
        for x in sorted(curmap.keys()) :
            ans += x
            ans += "" if curmap[x]==1 else str(curmap[x])
        return ans