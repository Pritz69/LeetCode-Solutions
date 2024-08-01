class Solution:
    def countSeniors(self, details: List[str]) -> int:
        c=0
        for x in details :
            if int(x[11:13]) > 60 :
                c +=1
        return c