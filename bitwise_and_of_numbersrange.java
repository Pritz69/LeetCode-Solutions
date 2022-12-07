class Solution {
    public int rangeBitwiseAnd(int left, int right) {
        int c=0;
        while (left!=right)
        {
            left=left>>1;
            right=right>>1;
            c +=1;
        }
        return left<<c;
    }
}
