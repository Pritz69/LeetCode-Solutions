class Solution:
    def minDeletions(self, s: str) -> int:
        d = defaultdict(int)
        for x in s :
            d[x] +=1
        res=0
        used=set()
        #print(d)
        for x in d :
            freq=d[x]
            while freq > 0  and freq in used :
                freq -=1
                res +=1
            used.add(freq)
        return res