class Solution {
    public int minimumPartition(String s, int k) {
        int ans = 1;
        long curr = 0;
        for(int i=0;i<s.length();i++){
            int digit = s.charAt(i)-'0';
            long temp = curr*10 + (long)digit;
            if(temp<=(long)k){
                curr = temp;
            }else{
                if(digit > k){
                    return -1;
                }
                ans++;
                curr = (long)digit;
            }
        }
        return ans;
    }
}
