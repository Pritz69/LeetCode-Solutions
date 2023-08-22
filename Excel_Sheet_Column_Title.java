class Solution {
    public String convertToTitle(int columnNumber) {
        String ans="";
        int rem=0;
        while(columnNumber>0)
        {
            rem=columnNumber%26;
            columnNumber=columnNumber/26;
            if(rem==0)
            {
                columnNumber -=1;
                rem=26;
            }
            char ch=(char)(rem+'A'-1); // char ch=(char)(rem+64);
            ans = ch + ans;
        }
        return ans;
    }
}
/*
class Solution {
    public String convertToTitle(int columnNumber) {
        String ans="";
        while(columnNumber>0)
        {
            columnNumber--; 
            char ch=(char)(columnNumber%26 + 'A');
            ans = ch + ans;
            columnNumber /= 26;
        }
        return ans;
    }
}
*/
