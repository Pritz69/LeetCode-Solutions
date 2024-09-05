class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m=len(rolls)
        avg=mean*(m+n)
        avg=avg-sum(rolls)
        ans=[]
        while n-1 :
            x=avg//n
            if x > 6 or x <= 0:
                return []
            ans.append(x)
            n -=1
            avg -=x
        if avg > 6 or avg <= 0:
            return []
        ans.append(avg)
        return ans