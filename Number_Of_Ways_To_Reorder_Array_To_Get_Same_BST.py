class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        n=len(nums)
        f=[1]*n
        for  i in range(1,n) :
            f[i] = f[i-1] * i
        def comb(l,r) :
            return f[l+r]//(f[l]*f[r])
        def ways(arr) :
            if len(arr)<=2 :
                return 1
            root = arr[0]
            left =[num for num in arr if num < root]
            right =[num for num in arr if num > root]
            return ways(left) * ways(right) * comb(len(left),len(right))
        return (ways(nums) -1) % (10**9 + 7)
