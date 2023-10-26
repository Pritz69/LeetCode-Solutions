class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod=10**9 + 7
        d={}
        arr.sort()
        for i in range(len(arr)) :
            d[arr[i]]=d.get(arr[i],0) + 1
            c=1
            for j in range(i) :
                if arr[i]%arr[j]==0 and (arr[i]//arr[j]) in d:
                    c += d[arr[j]] * (d[arr[i]//arr[j]])
            d[arr[i]]=c
        s=0
        for x in d :
            s +=d[x]
        return s%mod