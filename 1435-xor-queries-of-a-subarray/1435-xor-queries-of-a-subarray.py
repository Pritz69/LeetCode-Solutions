class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ans=[]
        xol=[]
        x=0
        for e in arr :
            x=x^e
            xol.append(x)
        xor=[0]*len(arr)
        xr=0
        for i in range(len(arr)-1,-1,-1) :
            xr=xr^arr[i]
            xor[i]=xr
        for q in queries :
            l,r=q[0],q[1]
            a=x
            if l-1 >= 0 :
                a=a^xol[l-1]
            if r+1 < len(arr) :
                a=a^xor[r+1]
            ans.append(a)
        return ans
        