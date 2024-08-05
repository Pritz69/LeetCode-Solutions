class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d={}
        for x in arr :
            d[x]=d.get(x,0)+1
        for i in range(len(arr)) :
            if d[arr[i]]==1 :
                k -=1
                if k==0 :
                    return arr[i]
        return ""