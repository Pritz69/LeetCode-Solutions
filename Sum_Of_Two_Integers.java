class Solution {
    public int getSum(int a, int b) {
        while(b!=0)
        {
            int tmp=(a&b)<<1;
            a=a^b;
            b=tmp;
        }
        return a;
    }
}
//https://assets.leetcode.com/users/images/c2e91add-95d5-44ef-8dc1-85d0e25219ad_1620502855.803335.png
/*
class Solution {
    public int getSum(int a, int b) {
        if(b==0)
        {
            return a;
        }
        int xo = a ^ b;  
        int c = a & b;   
        c = c << 1;            
        return getSum(xo,c);            
    }                           
}   
*/                              
