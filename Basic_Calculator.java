class Solution {
    public int calculate(String s) {
        int ans=0;
        int num=0;
        int sign=1;
        Stack<Integer>st=new Stack<>();
        for(int i=0;i<s.length();i++)
        {
            if (Character.isDigit(s.charAt(i)))
            {
                num=s.charAt(i)-'0';
                while(i+1<s.length() && Character.isDigit(s.charAt(i+1)))
                {
                    num=num*10 + (s.charAt(i+1)-'0');
                    i++;
                }
                num=num*sign;
                ans+=num;
                num=0;
            }
            else if(s.charAt(i)=='+')
            {
                sign=1;
            }
            else if(s.charAt(i)=='-')
            {
                sign=-1;
            }
            else if(s.charAt(i)=='(')
            {
                st.push(ans);
                st.push(sign);
                ans=0;
                sign=1;
            }
            else if(s.charAt(i)==')')
            {
                int psign=st.pop();
                ans=psign*ans;
                int pvans=st.pop();
                ans=ans+pvans;
            }
        }
        return ans;
    }
}
