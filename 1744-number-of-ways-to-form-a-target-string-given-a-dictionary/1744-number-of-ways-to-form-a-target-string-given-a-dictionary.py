class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        cnt=defaultdict(int)
        for w in words :
            for x,c in enumerate(w) :
                cnt[(x,c)] +=1
        dp={}
        def dfs(i,k) :
            if i==len(target):
                return 1
            if k==len(words[0]):
                return 0
            if (i,k) in dp :
                return dp[(i,k)]
            c=target[i]
            dp[(i,k)] = dfs(i,k+1)
            dp[(i,k)] += cnt[(k,c)]*dfs(i+1,k+1)
            return dp[(i,k)] % ((10**9) + 7)
        return dfs(0,0)