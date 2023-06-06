class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(len(arr)-2) :
            if abs(arr[i]-arr[i+1]) != abs(arr[i+1]-arr[i+2]) :
                return False
        return True
