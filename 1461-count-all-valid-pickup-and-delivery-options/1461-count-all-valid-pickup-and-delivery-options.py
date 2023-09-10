class Solution:
    def countOrders(self, n: int) -> int:
        ans=1
        slots= 2*n
        while slots > 0 :
            choices = (slots*(slots-1))//2
            ans = ans* choices
            slots -=2
        return ans%(10**9 + 7)