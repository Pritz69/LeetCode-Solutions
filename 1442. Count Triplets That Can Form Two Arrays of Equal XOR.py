class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans=0
        n=len(arr)
        for i in range(n-1) :
            a=0
            for j in range(i+1,n) :
                a=a^arr[j-1]
                b=0
                for k in range(j,n) :
                    b=b^arr[k]
                    if a==b :
                        ans +=1
        return ans



class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans=0
        n=len(arr)
        for i in range(n-1) :
           p=arr[i]
           for j in range(i+1,n) :
            p=p^arr[j]
            if p==0 :
                ans += j-i
        return ans
