# Time: O(nlogn) and  Space O(1)
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        arr.sort()
        res = []
        minDiff = float('inf')
        
        for i in range(n-1):
            minDiff = min(minDiff, arr[i+1]-arr[i])
            
        
        for i in range(n-1):
            if arr[i+1]-arr[i] == minDiff:
                res.append([arr[i], arr[i+1]])
                
        return res
