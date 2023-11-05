class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        st=1
        ma=max(arr[0],arr[1])
        if st==k :
            return ma
        for i in range(2,len(arr)) :
            if arr[i] > ma :
                st=1 
                ma = arr[i]
                if st==k :
                    return ma
            else :
                st +=1
                if st==k :
                    return ma
        return ma