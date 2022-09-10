class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length==0)
        {
            return 0;
        }
        int profit=0;
        for(int i=0;i<prices.length-1;i++)
        {
            if(prices[i]<prices[i+1])
            {
                profit += prices[i+1]-prices[i];
            }
        }
        return profit;
    }
}
