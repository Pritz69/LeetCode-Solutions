class Solution {
    private boolean isValid(int[] price, int taste, int k){
        int n = price.length;
        int prev = price[0];
        int k1 = k-1;
        for(int i=1;i<n && k1>0;i++){
            if(prev+taste<=price[i]){
                k1--;
                prev = price[i];
            }
        }
        if(k1 == 0){
            return true;
        }
        return false;
    }
    public int maximumTastiness(int[] price, int k) {
        Arrays.sort(price);
        int n = price.length;
        int ans = 0;
        int low = 0;
        int high = price[n-1]-price[0];
        while(low<=high){
            int mid = (low+high)/2;
            if(isValid(price,mid,k)){
                ans = Math.max(ans, mid);
                low = mid+1;
            }else{
                high = mid-1;
            }
        }
        return ans;
    }
}
