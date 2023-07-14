class Solution {
    public int longestSubsequence(int[] arr, int difference) {
        HashMap<Integer,Integer> h=new HashMap<>();
        int m=0;
        for (int i=0;i<arr.length;i++)
        {
            int x = arr[i]-difference;
            int c = h.getOrDefault(x,0) + 1;
            h.put(arr[i],c);
            m= Math.max(m,h.get(arr[i]));
        }
        return m;
    }
}
