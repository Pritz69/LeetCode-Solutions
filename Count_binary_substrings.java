class Solution {
    public int countBinarySubstrings(String s) {
        int count = 0, i = 1, prev = 0, curr = 1;
        while(i < s.length()) {
            //11000110
            if(s.charAt(i-1) != s.charAt(i)) {
                count+=Math.min(prev, curr);
                prev = curr;
                curr = 1;
            }
            else {
                curr++;
            }
            i++;
        }
        count+=Math.min(prev, curr);
        return count ;
    }
}
