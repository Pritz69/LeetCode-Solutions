class Solution {
    public String longestPalindrome(String s) {
	
        boolean [][] dp = new boolean [s.length()][s.length()];
	    String ans="";
        String temp= "";
		
        for(int gap=0;gap<s.length();gap++){
            for(int i=0,j=gap; j<dp.length;i++,j++){
			
                if(gap==0){
                    dp[i][j]=true;
                }
                else if(gap==1){
                if(s.charAt(i)==s.charAt(j)){
                    dp[i][j]=true;
                }
                else{
                    dp[i][j]=false;
                }
                }
                else{
                    if(s.charAt(i)==s.charAt(j) && dp[i+1][j-1]==true){
                        dp[i][j]=true;
                    }
                    else{
                        dp[i][j]=false;
                    }
                }
                if(dp[i][j]) {
					 temp = s.substring(i, j+1);
					 if(ans.length() < temp.length()) {
						 ans = temp;
                     }
                
                }
            }
        }
        return ans;
    }
}
