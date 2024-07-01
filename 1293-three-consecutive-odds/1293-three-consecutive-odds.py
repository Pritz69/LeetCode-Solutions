class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        f=0
        for i in range(len(arr)-2) :
            if arr[i]%2==1 and arr[i+1]%2==1 and arr[i+2]%2==1 :
                f=1
                return True
        if f==0 :
            return False