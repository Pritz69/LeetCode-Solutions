class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> st=new Stack<Integer>();
        int n=asteroids.length;
        for (int i=0;i<n;i++)
        {
            int e=asteroids[i];
            while (!st.isEmpty() && e<0 && st.peek()>0)
            {
                int diff= e + st.peek();
                if (diff < 0)
                {
                    st.pop();
                }
                else if(diff >0)
                {
                    e=0;
                }
                else if(diff==0)
                {
                    st.pop();
                    e=0;
                }
            }
            if(e !=0)
            {
                st.push(e);
            }
        }
        int s=st.size();
        int ans[]=new int[s];
        int i=0;
        while(i<s)
        {
            ans[i++]=st.pop();
        }
        int l=0;
        int r=s-1;
        while(l<=r)
        {
            int x=ans[r];
            ans[r]=ans[l];
            ans[l]=x;
            l +=1;
            r -=1;
        }
        return ans;
    }
}
