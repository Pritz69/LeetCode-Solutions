class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        curr = nums[0] + nums[1] + nums[2]
        
        
        #check ends
        if sum(nums[-3:]) <= target:

            return sum(nums[-3:])
        
        if sum(nums[:3]) >= target:

            return sum(nums[:3])
        
        for i in range(0, len(nums) - 2):
            repeated += 1
            l, r = i + 1, len(nums) - 1


            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            
            while l < r:
                s = nums[l] + nums[i] + nums[r]
                if abs(target - s) < abs(target - curr):
                    curr = s
                    
                elif s < target:
                    l += 1
                
                elif s > target:
                    r -= 1
                
                else:

                    return curr
            

        return curr
    
