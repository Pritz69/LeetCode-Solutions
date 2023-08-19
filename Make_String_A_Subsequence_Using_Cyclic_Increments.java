class Solution {
    public boolean canMakeSubsequence(String str1, String str2) {
        StringBuilder sb=new StringBuilder();
        for(int i=0;i<str1.length();i++)
        {
            char ch=str1.charAt(i);
            int as=ch;
            if(as==122)
            {
                as=97;
            }
            else if(as==121)                    // int asc = ch - 'a';
            {                                   // asc = (asc + 1) % 26;
                as=122;                         // char nc = (char) (asc + 'a');
            }
            else
            {
                as=(as+1)%122;
            }
            char nc=(char)as;
            sb.append(ch);
            sb.append(nc);
        }
        // System.out.print(sb);
        int i=0;
        int j=0;
        // int f=0;
        while(i+1<sb.length() && j<str2.length())
        {
            if ( (str2.charAt(j)==sb.charAt(i)) || (str2.charAt(j)==sb.charAt(i+1)) )
            {
                i +=2;
                j +=1;
            }
            else
            {
                i+=2;
            }
        }
        return j==str2.length();
    }
}
/*    public boolean canMakeSubsequence(String s1, String s2) {
        int j = 0, n = s1.length(), m = s2.length();
        for (int i = 0; i < n && j < m; ++i) {
            int a = s1.charAt(i), b = s2.charAt(j);
            if (a == b || a + 1 == b || a - 25 == b)
                ++j;
        }
        return j == m;
    }
*/
