class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        st="abcdefghijklmnopqrstuvwxyz"
        n = len(s)
        shift_effects = [0] * (n + 1)  

        for start, end, direction in shifts:
            if direction == 0:
                shift_effects[start] -= 1 
                shift_effects[end + 1] += 1
            else:
                shift_effects[start] += 1  
                shift_effects[end + 1] -= 1

        cumulative_shift = 0
        shift_amounts = []
        for shift in shift_effects[:-1]:
            cumulative_shift += shift
            shift_amounts.append(cumulative_shift % 26) 
        
        ans=list(s)
        for i in range(n) :
            ind=st.index(s[i])
            ind=(ind+shift_amounts[i])%26
            if ind < 0 :
                ind =(ind+ 26)%26
            ans[i]=st[ind]
        return "".join(ans)