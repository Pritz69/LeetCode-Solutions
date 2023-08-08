class Solution {
    public int accountBalanceAfterPurchase(int purchaseAmount) {
        int v=100-purchaseAmount;
        int b=0;
        while (v% 10 !=0)
        {
            b +=1;
            v -=1;
        }
        if (b<=5)
        {
            return (100-purchaseAmount)-b;
        }
        else
        {
            return (100-purchaseAmount)+(10-b);
        }
    }
}
