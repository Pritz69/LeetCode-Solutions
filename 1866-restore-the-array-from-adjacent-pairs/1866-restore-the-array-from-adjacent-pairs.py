class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        d={}
        dd=defaultdict(list)
        for x in adjacentPairs :
            d[x[0]]=d.get(x[0],0) + 1
            d[x[1]]=d.get(x[1],0) + 1
            dd[x[0]].append(x[1])
            dd[x[1]].append(x[0])
        st=0
        for x in d :
            if d[x]==1 :
                st=x
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


        
                    