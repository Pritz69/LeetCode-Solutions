class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a,b,c=0,0,0
        for x in nums :
            if x==0 :
                a +=1
            elif x==1 :
                b +=1
            else :
                c +=1
        for i in range(len(nums)) :
            if a > 0 :
                nums[i]=0
                a -=1
            elif b > 0 :
                nums[i]=1
                b-=1
            else :
                nums[i]=2
                c -=1
        print(nums)