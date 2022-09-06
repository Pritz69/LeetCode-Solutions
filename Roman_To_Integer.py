class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        total = 0  
        x = 0
        while x < len(s): 
            if s[x] == "I" and x + 1 < len(s) and (s[x + 1] == 'V' or s[x + 1] == 'X'): 
                total += (romans[s[x + 1]] - romans[s[x]])
                x += 2 
            elif s[x] == "X" and x + 1 < len(s) and (s[x + 1] == 'L' or s[x + 1] == 'C'):
                total += (romans[s[x + 1]] - romans[s[x]])
                x += 2
            elif s[x] == "C" and x + 1 < len(s) and (s[x + 1] == 'D' or s[x + 1] == 'M'):
                total += (romans[s[x + 1]] - romans[s[x]]) 
                x += 2
            else:
                total += romans[s[x]] 
                x += 1 
        return total
