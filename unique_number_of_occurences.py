class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        l=[]
        c=Counter(arr)
        for i in c:
            l.append(c[i])
        return (len(l)==len(set(l)))
