class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        res=0
        psum=0
        for i in satisfaction :
            psum += i
            if psum <0:
                break
            res +=psum
        return res
   
  
#TECH-WIRED
