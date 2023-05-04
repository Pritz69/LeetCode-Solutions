class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate =list(senate)
        d,r = deque(),deque()
        for i,v in enumerate(senate) :
            if v=='R' :
                r.append(i)
            else :
                d.append(i)
        while d and r :
            ds = d.popleft()
            rs = r.popleft()
            if ds <  rs :
                d.append(ds + len(senate))
            else :
                r.append(rs + len(senate))
        return 'Radiant' if r else 'Dire'
