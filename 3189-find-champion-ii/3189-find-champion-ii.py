class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        d=defaultdict(list)
        for x in edges :
            d[x[1]].append(x[0])
        l=[]
        for x in range(n) :
            if x not in d :
                l.append(x)
        if len(l) > 1 :
            return -1
        else :
            return l[0]