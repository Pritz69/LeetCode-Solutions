class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs(i,current,total):
            if total==target:
                res.append(current.copy())
                return 
            if i>=len(candidates) or total>target:
                return
            current.append(candidates[i])
            dfs(i,current,total+candidates[i])
            current.pop()
            dfs(i+1,current,total)
        dfs(0,[],0)
        return res
