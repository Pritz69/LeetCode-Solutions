class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n=len(arr)
        c=0
        ans=[]
        for i in range(n) :
            for j in range(n-1,-1,-1) :
                ans.append((arr[i],arr[j],arr[i]/arr[j]))
        ans.sort(key=lambda x:x[2])
        return ans[k-1][:2]
