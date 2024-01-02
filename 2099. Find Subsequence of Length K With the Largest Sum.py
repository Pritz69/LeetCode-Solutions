class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        l=[]
        for i,v in enumerate(nums) :
            l.append((v,i))
        l.sort(reverse=True)
        nl=[]
        for i in range(k) :
            nl.append(l[i])
        nl.sort(key=lambda x:x[1])
        ans=[]
        for x in nl :
            ans.append(x[0])
        #print(l,nl,ans)
        return ans
