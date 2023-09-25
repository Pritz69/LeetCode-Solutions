class Solution {
    public char findTheDifference(String s, String t) {
        int sm=0;
        for (int i=0;i<t.length();i++)
        {
            sm += t.charAt(i);
        }
        for (int i=0;i<s.length();i++)
        {
            sm -= s.charAt(i);
        }
        return (char)sm ;
    }
}