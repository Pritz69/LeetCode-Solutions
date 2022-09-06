class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& mat, int r, int c) {
        vector<vector<int>>ans(r,vector<int>(c));
        int m = mat.size();
        int n = mat[0].size();
        if(r*c!=m*n)
            return mat;
        int rows=0;
        int cols=0;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                ans[rows][cols]=mat[i][j];
                cols++;
                if(cols==c){
                    rows++;
                    cols=0;
                }
            }
        }
     return ans;   
    }
};
