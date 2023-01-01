class Solution {
    
    List<Integer> primes = new ArrayList<>();
    
    private void sieveOfEratosthenes(int n){
        boolean prime[] = new boolean[n+1];
        for(int i=0;i<=n;i++)
            prime[i] = true;
         
        for(int p = 2; p*p <=n; p++){
            if(prime[p] == true){
                for(int i = p*p; i <= n; i += p)
                    prime[i] = false;
            }
        }
        for(int i = 2; i <= n; i++)
        {
            if(prime[i] == true)
                primes.add(i);
        }
    }
    public int[] closestPrimes(int left, int right) {
        sieveOfEratosthenes(right);
        int[] ans = new int[2];
        
        int minDiff = Integer.MAX_VALUE;
        int v1 = -1;
        int v2 = -1;
        int i = 0;
        for(i=0;i<primes.size();i++){
            if(primes.get(i)>=left){
                break;
            }
        }
        for(int j=i+1;j<primes.size();j++){
            int currDiff = primes.get(j)-primes.get(j-1);
            if(currDiff<minDiff){
                minDiff = currDiff;
                v1 = primes.get(j-1);
                v2 = primes.get(j);
            }
        }
        ans[0] = v1;
        ans[1] = v2;
        return ans;
    }
}
