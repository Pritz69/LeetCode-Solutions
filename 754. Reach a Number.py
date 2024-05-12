class Solution:
    def reachNumber(self, target: int) -> int:
        steps=0
        sum=0
        target=abs(target)
        while (sum < target) :
            sum += steps
            steps +=1
        while (sum-target)%2 != 0 :
            sum += steps 
            steps +=1
        return steps-1
