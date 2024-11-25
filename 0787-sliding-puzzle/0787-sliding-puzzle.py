class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        adj={0:[1,3],1:[0,2,4],2:[1,5],3:[0,4],4:[1,3,5],5:[2,4]}
        b="".join([str(c) for row in board for c in row])
        q=deque([(b.index('0'),b,0)])
        visit=set([b])
        while q :
            i,b,l=q.popleft()
            if b=="123450" :
                return l
            ba=list(b)
            for j in adj[i] :
                nb=ba.copy()
                nb[i],nb[j]=nb[j],nb[i]
                nb="".join(nb)
                if nb not in visit :
                    visit.add(nb)
                    q.append((j,nb,l+1))
        return -1