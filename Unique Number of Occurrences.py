class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c=Counter(arr)
        s=set()
        for x in c :
            if c[x] in s :
                return False
            else :
                s.add(c[x])
        return True
        
