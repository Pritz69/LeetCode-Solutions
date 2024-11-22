class Solution {
    public int maxEqualRowsAfterFlips(int[][] matrix) {
        Map<String, Integer> map = new HashMap<>();
        
        for (int[] row : matrix) {
            StringBuilder key = new StringBuilder();
            StringBuilder flippedKey = new StringBuilder();
            
            for (int num : row) {
                key.append(num);
                flippedKey.append(1 - num); // Flip the bit
            }
            
            // Convert to string representation for the map key
            String normalKey = key.toString();
            String flipKey = flippedKey.toString();
            
            if (row[0]==1)
            {
                normalKey=flipKey;
            }
            map.put(normalKey, map.getOrDefault(normalKey, 0) + 1);
        }
        int maxCount = 0;
        for (int count : map.values()) {
            maxCount = Math.max(maxCount, count);
        }
        return maxCount;
    }
}