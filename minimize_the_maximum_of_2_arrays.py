class Solution:
    def minimizeSet(self, D1: int, D2: int, C1: int, C2: int) -> int:
        
        L, R, G = 0, 10**10, lcm(D1, D2)

        while L < R:
            
            M = (L+R)//2                # [0] try middle value
            
            x = M - M//D1 >= C1         # [1] criterion 1
            y = M - M//D2 >= C2         # [2] criterion 2
            z = M - M//G  >= C1 + C2    # [3] criterion 3
            
            if x and y and z :
                 R = M    
            else             :
                 L = M+1  
        return L
