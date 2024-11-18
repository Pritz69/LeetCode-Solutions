class Solution:
    def decrypt(self, arr: List[int], k: int) -> List[int]:
        if k==0 :
            return [0]*len(arr)
        elif k > 0 :
            ans=[]
            for i in range(len(arr)) :
                s=0
                for j in range(1,k+1) :
                    s += arr[(i+j)%len(arr)]
                ans.append(s)
            return ans
        else :
            ans=[]
            for i in range(len(arr)) :
                s=0
                for j in range(1,abs(k)+1) :
                    if (i-j) < 0 :
                        s += arr[i-j+len(arr)]
                    else :
                        s += arr[i-j]
                ans.append(s)
            return ans
                