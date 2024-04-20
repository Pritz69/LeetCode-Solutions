class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        def dfs(i,j) :
            nonlocal ei, ej
            if i<0 or j<0 or i>=m or j>=n or land[i][j]==0 :
                return
            ei=max(i,ei)
            ej=max(j,ej)
            land[i][j]=0
            dfs(i+1,j)
            dfs(i,j+1)
        m,n=len(land),len(land[0])
        ans=[]
        for i in range(m) :
            for j in range(n) :
                if land[i][j]==1 :
                    ei,ej=i,j
                    dfs(i,j)
                    ans.append([i,j,ei,ej])
        return ans



class Solution {
public:
    vector<vector<int>> findFarmland(vector<vector<int>>& land) {
        int m = land.size();
        int n = land[0].size();
        
        vector<vector<int>> result;
        for(int i = 0; i<m; i++) {
            for(int j = 0; j<n; j++) {
                
                //We have to deal with 1s only
                if(land[i][j] == 0) continue;

                //Find right most column of rectangle (see the image below)
                int c1 = j;
                while(c1 < n && land[i][c1] == 1) {
                    c1++;
                }

                //Find bottom most row of rectangle (see the image below)
                int r2 = i;
                while(r2 < m && land[r2][j] == 1) {
                    r2++;
                }
                
                //Then you can find bottom right most of rectangle
                c1 = c1==0 ? c1 : c1-1;
                r2 = r2==0 ? r2 : r2-1;

                //Use them as your answer
                //{r1, c1} = {i, j}
                //{r2, c2} = {r2, c1}
                result.push_back({i, j, r2, c1});
                
                //Now, mark the covered land with 0 so that you don't consider them later
                for(int k = i; k<=r2; k++) {
                    for(int l = j; l<=c1; l++) {
                        land[k][l] = 0;
                    }
                }
                
            }
        }
        return result;
    }
};
