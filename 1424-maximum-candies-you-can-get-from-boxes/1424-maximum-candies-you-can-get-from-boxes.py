class Solution:
    def maxCandies(self, st: List[int], can: List[int], keys: List[List[int]], cBoxes: List[List[int]], iBoxes: List[int]) -> int:
        ans=0
        vc=set()
        q=deque(iBoxes)
        box=set()
        while q :
            i=q.popleft()
            if i not in vc:
                box.add(i)
                vc.add(i)
            for x in keys[i] :
                if x != i :
                    st[x]=1
            for x in cBoxes[i] :
                if x not in vc :
                    q.append(x)
        print(st)
        for i in box :
            if st[i]==1 :
                ans += can[i]
        return ans
