class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shift_effects = [0] * (n + 1)  
        for start, end, direction in shifts:
            if direction == 0:
                shift_effects[start] -= 1 
                shift_effects[end + 1] += 1
            else:
                shift_effects[start] += 1  
                shift_effects[end + 1] -= 1

        for i in range(1,n) :
            shift_effects[i] = (shift_effects[i-1]+shift_effects[i])%26
        
        ans=list(s)
        for i in range(n) :
            ind=( (ord(s[i])-97) + shift_effects[i])%26
            if ind < 0 :
                ind =ind+ 26
            ans[i]=chr(97+ind)
        return "".join(ans)