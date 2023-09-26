class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                l = j + 1
                r = len(nums) - 1
                while l < r:
                    tot = nums[i] + nums[j] + nums[l] + nums[r]
                    if tot == target:
                        result.append([nums[i], nums[j], nums[l], nums[r]])
                        l+=1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif tot < target:
                        l += 1
                    else:
                        r -= 1
        return result
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
            nums.sort()
            res=[]
            quad=[]
            def ksum(k,st,tar) :
                if k!=2 :
                    for i in range(st,len(nums)-k+1) :
                        if i>st and nums[i]==nums[i-1] :
                            continue
                        quad.append(nums[i])
                        ksum(k-1,i+1,tar-nums[i])
                        quad.pop()
                    return 
                l=st
                r=len(nums)-1
                while l<r :
                    if nums[l] + nums[r] < tar:
                        l +=1
                    elif nums[l] + nums[r] > tar :
                        r -=1
                    else :
                        # quad.append(nums[l])
                        # quad.append(nums[r])
                        # res.append(quad[:])
                        # quad.pop()
                        # quad.pop()
                        res.append( quad + [nums[l],nums[r]] )
                        l +=1
                        while l<r and nums[l]==nums[l-1] :
                            l +=1
            ksum(4,0,target)
            return res