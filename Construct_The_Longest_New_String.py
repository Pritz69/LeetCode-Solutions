class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        c=min(x,y)
        if x==y :
            return (c+c+z)*2
        else :
            return (c+c+1+z)*2

            
