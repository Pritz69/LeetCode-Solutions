class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        l = []
        for x in timePoints:
            f = int(x[:2])  
            s = int(x[3:]) 
            m = f * 60 + s  
            l.append(m)

        l.sort()  
        ans = float('inf')

        
        for i in range(1, len(l)):
            ans = min(ans, l[i] - l[i-1])
            
        ans = min(ans, 1440 - (l[-1] - l[0]))        

        return ans
            