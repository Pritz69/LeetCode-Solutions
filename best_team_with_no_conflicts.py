class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        pairs=[[scores[i],ages[i]] for i in range(len(scores))]
        pairs.sort()
        dp=[pairs[i][0] for i in range(len(pairs))]
        for i in range(len(pairs)) :
            score,age=pairs[i]
            for j in range(i) :
                sc,a=pairs[j]
                if age >= a :
                    dp[i]=max(dp[i],score+dp[j])
        return max(dp)
