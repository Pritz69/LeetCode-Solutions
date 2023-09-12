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
            #while freq > 0  and freq in used :
            #    freq -=1
            #    res +=1
            #used.add(freq)
            while freq in used :
                freq -=1
                res +=1
            if freq==0 :
                continue # no point of considering it anymore as it is already completely deleted and 0 wont get counted!
            else :
                used.add(freq)
        return res