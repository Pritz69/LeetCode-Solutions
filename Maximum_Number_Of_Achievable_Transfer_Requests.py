class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        ans = 0
        arr = [0]*n
        def backtrack(ind,cnt,arr) :
            nonlocal ans
            if ind==len(requests) :
                for x in arr :
                    if x<0 :
                        return
                ans=max(ans,cnt)
                return 
                
            arr[requests[ind][0]] -=1
            arr[requests[ind][1]] +=1
            backtrack(ind+1,cnt+1,arr)

            arr[requests[ind][0]] +=1
            arr[requests[ind][1]] -=1

            backtrack(ind+1,cnt,arr)

        backtrack(0,0,arr)
        return ans
