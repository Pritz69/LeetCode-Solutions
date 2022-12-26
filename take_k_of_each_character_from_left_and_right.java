class Solution {
    
    private boolean isSatisfied(int[] freq, int k){
        return freq[0]>=k && freq[1]>=k && freq[2]>=k;
    }
    
    private boolean isValid(String s, int k, int ct){
        int[] freq = new int[3];
        int l = s.length();
        for(int i=0;i<ct;i++){
            freq[s.charAt(i)-'a']++;
        }
        if(isSatisfied(freq,k)){
            return true;
        }
        
        int left = ct-1;
        int right = l-1;
        while(left>=0){
            freq[s.charAt(left--)-'a']--;
            freq[s.charAt(right--)-'a']++;
            if(isSatisfied(freq,k)){
                return true;
            }
        }
        return false;
    }
    
    public int takeCharacters(String s, int k) {
        int ans = Integer.MAX_VALUE;
        int l = s.length();
        int low = 0;
        int high = l;
        while(low<=high){
            int mid = (low+high)/2;
            if(isValid(s,k,mid)){
                ans = Math.min(ans, mid);
                high = mid-1;
            }else{
                low = mid+1;
            }
        }
        if(ans == Integer.MAX_VALUE){
            ans = -1;
        }
        return ans;
    }
}
