class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        s,l=arrays[0][0],arrays[0][-1]
        ans=0
        for i in range(1,len(arrays)) :
            ans=max(ans, abs(arrays[i][-1]-s) , abs(l-arrays[i][0]))
            s=min(s,arrays[i][0])
            l=max(l,arrays[i][-1])        
        return ans
