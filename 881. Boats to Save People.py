class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l,r=0,len(people)-1
        res=0
        while l<=r :
            rem = limit - people[r]
            res +=1
            r -=1 
            if rem >= people[l] :
                l +=1 
        return res
