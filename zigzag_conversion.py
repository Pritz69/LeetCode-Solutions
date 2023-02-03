class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res=[]
        if numRows==1 :
            return s
        for r in range(numRows) :
            inc = 2*(numRows-1)
            for i in range(r,len(s),inc) :
                res.append(s[i])
                if (r > 0 and r < numRows-1 and (i + inc - 2 * r)< len(s)):
                    res.append(s[i+inc-(2*r)])
        return ''.join(res)
                
