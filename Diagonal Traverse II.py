class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        d=defaultdict(list)
        for i in range(len(nums)-1,-1,-1) :
            for j in range(len(nums[i])-1,-1,-1) :
                d[i+j].append(nums[i][j])
        ans=[]
        #nd=dict(sorted(d.items(), key = lambda x: x[0]))
        #print(nd)
        #for x in nd :
        #    l=d[x]
        #    #l.sort(reverse=True)
        #    ans = ans + l
        m=0
        for x in d :
            m=max(m,x)
        for i in range(m+1) :
            ans +=d[i]
        return ans
