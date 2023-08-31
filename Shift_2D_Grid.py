class Solution {
public:
    vector<vector<int>> shiftGrid(vector<vector<int>>& grid, int k) {
        int n=grid.size();
        int m=grid[0].size();
        vector<vector<int>> ans(n,vector<int>(m));
        
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                
                int newJ=(j+k)%m; // (j + numbers of columns added)%m
                
                int newI=(i+(j+k)/m)%n; // (i + numbers of rows added)%n 
                
                ans[newI][newJ]=grid[i][j];
            }
        }
        return ans;
    }
};
# BRUTE FORCE APPROACH 
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        
        for _ in range(k):
            prev = grid[-1][-1]
            
            for row in range(rows):
                for col in range(cols):
                    temp = grid[row][col]
                    grid[row][col] = prev
                    prev = temp
        
        return grid
