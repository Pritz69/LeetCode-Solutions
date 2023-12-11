class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n=len(arr)
        c=n//4
        Co=Counter(arr)
        for x in Co :
            if Co[x] > c :
                return x
        return 0
