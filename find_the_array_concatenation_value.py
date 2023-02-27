class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        s=0
        l=0
        r=len(nums)-1
        li=[]
        if len(nums)%2 == 1 :
            while l<r :
                st =int(str(nums[l])+str(nums[r]))
                li.append(st)
                s +=st
                l +=1
                r -=1
            s +=int(nums[l])
        else :
            while l<r :
                st =int(str(nums[l])+str(nums[r]))
                li.append(st)
                s +=st
                l +=1
                r -=1
        return s
