class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        C=Counter(text)
        B=Counter("balloon")
        res=float("inf")
        for i in B :
            res=min(res,C[i]//B[i])
        return res
