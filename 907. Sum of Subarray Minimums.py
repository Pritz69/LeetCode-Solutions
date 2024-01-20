class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n=len(arr)
        mod=10**9 + 7
        nxtsma=[0]*n
        prevsma=[0]*n
        for i in range(n) :
            nxtsma[i]=n-i-1  #base case when there is no smaller elem,so taking all the available elements after this(excluding curr)
            prevsma[i]=i    #base case, when there is no smaller elem,so taking all the available elements before this(excluding curr)
        st=[]
        for i in range(n) :
            while st and arr[i] < st[-1][1] :
                nxtsma[st[-1][0]]=i-st[-1][0]-1
                st.pop()
            st.append((i,arr[i]))
        #print(nxtsma)
        st=[]
        for i in range(n-1,-1,-1) :
            while st and arr[i] <= st[-1][1] :
                prevsma[st[-1][0]]=st[-1][0]-i-1
                st.pop()
            st.append((i,arr[i]))
        #print(prevsma)
        ans=0
        for i in range(n) :
            left=prevsma[i]
            right=nxtsma[i]
            v= ( (arr[i]*(left +1))%mod * (right+1) )%mod
            ans = (ans + v)%mod
        return ans
