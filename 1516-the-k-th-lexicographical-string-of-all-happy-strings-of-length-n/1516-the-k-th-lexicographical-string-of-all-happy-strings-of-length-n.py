
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
    # array with one element so it can be mutated w/ in backtrack, otherwise just use nonlocal
        happyString = [""] 
        count = [0]

        def backtrack(cur):
            if count[0] == k: 
                return 

            if len(cur) == n:
                happyString[0] = cur
                count[0] += 1 
                return

            for c in ['a', 'b', 'c']:
                if len(cur) > 0 and cur[-1] == c:
                    continue
                backtrack(cur + c)

        backtrack("")
        return happyString[0] if count[0] == k else ""

