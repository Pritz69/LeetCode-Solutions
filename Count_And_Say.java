class Solution {
    public String countAndSay(int n) {
        String s="1";
        for(int i=2;i<=n;i++)
        {
            s=Final(s);
        }
        return s;
    }
    public String Final(String s)
    {
        StringBuilder sb=new StringBuilder();
        char c=s.charAt(0);
        int cnt=1;
        for(int i=1;i<s.length();i++)
        {
            if(s.charAt(i)==c)
            {
                cnt ++;
            }
            else
            {
                sb.append(cnt);
                sb.append(c);
                c=s.charAt(i);
                cnt=1;
            }
        }
        sb.append(cnt);
        sb.append(c);
        return sb.toString();
    }
}
