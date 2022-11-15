class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        output=[""]
        for c in s:
            t=[]
            if c.isalpha():
                for o in output:
                    t.append(o+c.upper())
                    t.append(o+c.lower())
            else:
                for o in output:
                    t.append(o+c)
            output=t
        return output
