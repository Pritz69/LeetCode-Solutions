class Solution:
    def arrangeCoins(self, n: int) -> int:
        k = 1
        
        while n >= 0:
            n -= k
            k += 1
            
        return k - 2
      
      class Solution:
    def arrangeCoins(self, n: int) -> int:
        l=1
        r=n
        res=0
        while l<=r:
            m=(l+r)//2
            coins=(m/2)*(m+1)
            if coins>n:
                r=m-1
            else:
                l=m+1
                res=max(m,res)
        return res
