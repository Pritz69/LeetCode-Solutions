class Solution {
    public String decodeAtIndex(String s, int k) {
        long size=0;
        int n=s.length();
        for(char x:s.toCharArray())
        {
            if(Character.isDigit(x))
            {
                size *= (x-'0');
            }
            else 
            {
                size +=1;
            }
        }
        for(int i=n-1;i>=0;i--)
        {
            char c=s.charAt(i);
            k %= size;
            if((k==0 || k==size) && Character.isLetter(c))
            {
                return Character.toString(c);
            }
            if(Character.isDigit(c))
            {
                size=size/(c-'0');
            }
            else
            {
                size -=1;
            }
        }
        return null;
    }
}