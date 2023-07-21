class Solution {
    public List<Integer> largestDivisibleSubset(int[] arr) {
        Arrays.sort(arr);
        int dp[]=new int[arr.length];
        int hash[]=new int[arr.length];
        int m=0;
        int lastidx=0;
        for(int i=0;i<arr.length;i++)
        {
            dp[i]=1;
            hash[i]=i;
            for(int j=0;j<i;j++)
            {
                if(arr[i]%arr[j]==0 && ((1+dp[j])>dp[i]))
                {
                    dp[i]= 1+dp[j];
                    hash[i]=j;
                }
            }
            if(dp[i]>m)
            {
                m=dp[i];
                lastidx=i;
            }
        }
        Stack<Integer> st=new Stack<Integer>();
        st.push(arr[lastidx]);
        while(hash[lastidx]!=lastidx)
        {
            lastidx=hash[lastidx];
            st.push(arr[lastidx]);
        }
        ArrayList<Integer> ans=new ArrayList<Integer>();
        for(int i=0;i<m;i++)
        {
            ans.add(st.pop());
        }
        return ans;
    }
}
