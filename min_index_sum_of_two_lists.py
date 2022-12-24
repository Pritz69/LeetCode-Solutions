class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        fav = {r:i for i,r in enumerate(list1)}
        res = []
        min_ix = float('inf')
        for i, r in enumerate(list2):
            if r in fav:
                if i + fav[r] == min_ix:
                    res.append(r)
                elif i + fav[r] < min_ix:
                    res = [r]
                    min_ix = i + fav[r]
        return res

