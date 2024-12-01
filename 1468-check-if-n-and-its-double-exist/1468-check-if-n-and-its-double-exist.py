class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s=set(arr)
        for x in arr :
            if x!=0 and x*2 in s :
                return True
            if x==0 and arr.count(0) >= 2 :
                return True
        return False