class Solution {
    public int countSeniors(String[] details) {
        int ans = 0;
        for (String st : details) {
            int x = st.charAt(11);
            if (x > '6') {
                ans++;
            } else if (x == '6') {
                if (st.charAt(12) > '0') ans++;
            }
        }
        return ans;
    }
}