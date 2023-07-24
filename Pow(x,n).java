class Solution {  
    private double pow(double x, long n) {
        if (n == 0) 
        {
            return 1;
        }
        if (n % 2 == 0) 
        {
            return pow(x * x, n / 2);
        }
        else
        {
            return x * pow(x * x, (n - 1) / 2);
        } 
    }
    public double myPow(double x, int n) 
    {
        if (n < 0) 
        {
            return 1.0 / pow(x, (long) -1 * n);
        }
        return pow(x, (long) n);
    }
}
