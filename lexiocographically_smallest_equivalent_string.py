class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        UF = {}
        def find(x):
            UF.setdefault(x,x)
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x,y):
            rootX = find(x)
            rootY = find(y)
            # The main issue we need to take care of in this problem is
            # that we want the root of a group to be 
            # the smallest element in the group
            # So every time we add an element in a group, we check if it is the smallest one,
            # If it is, we set it as the root.
            if rootX>rootY:
                UF[rootX] = rootY
            else:
                UF[rootY] = rootX
        
        # Union the two equivalent characters
        # at the same position from s1 and s2 into the same group.
        for i in range(len(s1)):
            union(s1[i],s2[i])
        
        # Simply find the root of the group a character belongs to
        # Note that if c is not in any group, 
        # we have UF.setdefault(x,x) in def find(x) to take care of it
        res = []
        for c in baseStr:
            res.append(find(c))
            
        return ''.join(res)
