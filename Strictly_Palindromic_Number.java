class Solution {
    public boolean isStrictlyPalindromic(int n) {
      
      // toString(int i, int radix) method of Integer class 
      // i: the int value that we want to convert 
      // the radix or base to be used in getting the string representation of int method argument
 
      for(int i=2;i<=n-2;i++){
          if( !checkPalindrome(Integer.toString(n,i)) )   
          return false;
      }
      return true;
    }
    
    public boolean checkPalindrome(String s){
        
        for(int i=0;i<s.length()/2;i++){
            
            if( !(s.charAt(i) == s.charAt(s.length()-i-1)) )
            return false;
        }
        return true;
    }
}
