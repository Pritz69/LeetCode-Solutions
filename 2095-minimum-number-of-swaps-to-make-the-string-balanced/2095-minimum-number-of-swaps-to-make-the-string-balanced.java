class Solution {
    public int minSwaps(String s) {
        int count = 0;
        int stackSize = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '[') {
                stackSize++;
            } else if (stackSize == 0) {
                count++;
            } else {
                stackSize--;
            }
        }
        
        return (count + 1) / 2;
    }
}