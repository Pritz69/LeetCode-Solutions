class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for x in strs :
            l=list(x)
            l.sort()
            d["".join(l)].append(x)
        return list(d.values())
