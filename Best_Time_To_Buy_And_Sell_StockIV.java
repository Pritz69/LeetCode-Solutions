class Solution {
    public int maxProfit(int k, int[] prices) {
        int l=prices.length;
        if(l <=1 || k <=0)
        {
            return 0;
        }
        int p=0;
        if(k>=l/2)
        {
            for(int i =0;i<l-1;i++)
            {
                if(prices[i]<prices[i+1])
                {
                 p +=prices[i+1]-prices[i];
                }
            }
            return p;
        }
        int buy[]=new int[k];
        Arrays.fill(buy,Integer.MIN_VALUE);
        int sell[]=new int[k];
        for (int i=0;i<prices.length;i++)
        {
           for(int j=0;j<k;j++)
           {
               buy[j]=Math.max(buy[j],j==0 ? 0-prices[i] :sell[j-1]-prices[i]);
               sell[j]=Math.max(sell[j],buy[j]+prices[i]);
           }
        }
        return sell[k-1];
    }
}
