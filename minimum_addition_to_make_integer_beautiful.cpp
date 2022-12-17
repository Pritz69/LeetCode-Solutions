class Solution {
public:
    long long makeIntegerBeautiful(long long n, int target) {
        
        long long ans=0, sum=0, i, j, mul;
        
        j=n;
        
        while(j>0){
            sum=sum+(j%10);
            j/=10;
        }
        
        mul=1;
        while(sum>target){
            
            
            
            while((n%mul)==0){
                mul=mul*10;
            }
            ans=ans+mul-(n%mul);
            n=n+mul-(n%mul);
            
            
            j=n;
            sum=0;
            
            while(j>0){
                sum=sum+(j%10);
                j/=10;
            }
        }
        
        return ans;
        
    }
};
