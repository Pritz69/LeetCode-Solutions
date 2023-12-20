class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        m,sm=float('inf'),float('inf')
        for x in prices :
            if x < m :
                sm=m
                m=x
            elif x < sm :
                sm=x
        #print(m,sm)
        if (m+sm) > money :
            return money
        else :
            return money-(m+sm)
