class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        dd=defaultdict(list)
        for x in adjacentPairs :
            dd[x[0]].append(x[1])
            dd[x[1]].append(x[0])
        st=0
        for x in dd :
            if len(dd[x])==1 :
                st=x
                break
        l=[]
        s=set()
        q=deque()
        q.append(st)
        s.add(st)
        while q:
            n=q.popleft()
            l.append(n)
            for v in dd[n] :
                if v not in s :
                    s.add(v)
                    q.append(v)
        return l    


        
                    