class Solution:
    def maxLength(self, arr: List[str]) -> int:
        chset=set()
        def repeat(chset,neww):
            ws=set()
            for c in neww :
                if c in chset or c in ws :
                    return True
                ws.add(c)
            return False
        def backtrack(i) :
            if i==len(arr) :
                return len(chset)
            restk=0
            if not repeat(chset,arr[i]) :
                for c in arr[i] :
                    chset.add(c)
                restk=backtrack(i+1)
                for c in arr[i] :
                    chset.remove(c)
            resntk=backtrack(i+1)
            return max(restk,resntk)
        return backtrack(0)
