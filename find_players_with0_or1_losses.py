class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans=[[]for i in range(2)]
        losscount=Counter()
        for winner,loser in matches:
            if winner not in losscount:
                losscount[winner]=0
            losscount[loser] +=1
        for player,numloss in losscount.items():
            if numloss<2:
                ans[numloss].append(player)
        return [sorted(ans[0]),sorted(ans[1])]
