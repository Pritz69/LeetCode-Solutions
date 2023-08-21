class Solution {
    public boolean repeatedSubstringPattern(String s) {
        StringBuilder sb=new StringBuilder(s);
        sb.append(s);
        String s1=sb.substring(1,sb.length()-1);
        if(s1.contains(s))
        {
            return true;
        }
        return false;
    }
}
/*
class Solution {
    public boolean repeatedSubstringPattern(String s) {
        StringBuilder sb=new StringBuilder(s);
        for(int i=0;i<sb.length()/2;i++)
        {
            char ch=sb.charAt(0);
            sb.append(ch);
            sb.delete(0,1);
            if(sb.toString().equals(s))
            {
                return true;
            }
        }
        return false;
    }
}
*/
