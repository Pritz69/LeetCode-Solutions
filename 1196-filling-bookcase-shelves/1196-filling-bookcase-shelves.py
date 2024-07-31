class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        def func(i) :
            if i==len(books) :
                return 0
            if i in dp :
                return dp[i]
            dp[i]=float('inf')
            maxh=0
            curw=shelfWidth
            for j in range(i,len(books)) :
                w,h=books[j]
                if curw < w :
                    break
                maxh=max(maxh,h)
                curw -=w
                dp[i]=min(dp[i],func(j+1)+maxh)
            return dp[i]
        dp={}
        return func(0)