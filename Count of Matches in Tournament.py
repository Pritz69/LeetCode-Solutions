class Solution:
    def numberOfMatches(self, n: int) -> int:
        c=0
        while n != 1 :
            if n%2==0 :
                c += n//2
                n = n//2
            else :
                c += n//2
                n = n//2 + 1
        return c

# return n-1
