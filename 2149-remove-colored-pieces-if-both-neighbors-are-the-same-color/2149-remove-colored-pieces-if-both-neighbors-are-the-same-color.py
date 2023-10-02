class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        ta=0
        tb=0
        for i in range(2,len(colors)):
            if colors[i]=='A' and colors[i-1]=='A' and colors[i-2]=='A' :
                ta +=1
            elif colors[i]=='B' and colors[i-1]=='B' and colors[i-2]=='B' :
                tb +=1
        if ta>tb :
            return True
        else :
            return False