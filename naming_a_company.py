class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        wordmap=collections.defaultdict(set)
        for w in ideas :
            wordmap[w[0]].add(w[1:])
        res=0
        for c1 in wordmap :
            for c2 in wordmap :
                if c1==c2 :
                    continue
                intersect=0
                for w in wordmap[c1] :
                    if w in wordmap[c2] :
                        intersect +=1
                dist1= len(wordmap[c1])-intersect
                dist2= len(wordmap[c2])-intersect
                res += (dist1*dist2)
        return res
