class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        q=time//(n-1)
        r=time%(n-1)
        if q % 2 == 0:      
            return 1 + r   
        return n - r       
