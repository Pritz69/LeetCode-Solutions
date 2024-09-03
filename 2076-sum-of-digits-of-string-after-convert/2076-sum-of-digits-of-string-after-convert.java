class Solution {
    public int getLucky(String s, int k) {
        int sum = 0;
        for (char ch : s.toCharArray()) {
            int a = ch - 96;
            sum += a % 10;     
            a /= 10;
            sum += a;  
        }
        k--;   
        while (k > 0) {
            int temp = sum;
            sum = 0;
            while (temp != 0) {
                sum += temp % 10;
                temp /= 10;
            }
            k--;
        }
        return sum;
    }
}