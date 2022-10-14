class Solution {
    public int reversePairs(int[] nums) {
        
        int ans =  mergesort(nums,0,nums.length-1);
        return ans ;
    }
    public static int mergesort(int[] arr, int l , int r  ){
        
        if(l>=r){
            return 0;
        }
            int mid = (l+r)/2;
            int count = mergesort(arr,l,mid);
            count += mergesort(arr,mid+1,r);
            count += merge(arr,l,mid,r);
        
        return count;
    }
    public static int merge(int[] arr, int l , int mid, int r ){
        int count = 0;
        int j = mid+1;
        
        for(int i=l;i<=mid;i++){
            while(j<=r && arr[i] > (2 *(long) arr[j] ) ){
                j++;
            }
            count += (j- (mid+1)) ;
        }
       ArrayList<Integer> temp = new ArrayList<>(); 
        int i =l, idx = l;
        j = mid+1;
        while(i<= mid && j<=r ){
            if(arr[i]<=arr[j] ){
                temp.add(arr[i++] );
            }else{
                temp.add(arr[j++] );

            }
        }
        while(i<=mid){
            temp.add(arr[i++] );
        }
        while(j<= r){
            temp.add(arr[j++] );
        }
        for( i=l;i<=r;i++){
            arr[i] = temp.get(i-l);
        }
        return count;
    }
    
}
