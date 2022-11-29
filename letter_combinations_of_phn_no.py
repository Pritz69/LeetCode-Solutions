class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        digittochar={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        def backtrack(i,curstrng):
            if len(curstrng)==len(digits):
                res.append(curstrng)
                return
            for c in digittochar[digits[i]]:
                backtrack(i+1,curstrng+c)
        if digits:
            backtrack(0,"")
        return res
