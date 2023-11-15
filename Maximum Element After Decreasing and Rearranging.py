class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        m=1
        for i in range(len(arr)) :
            m=min(m,arr[i])
            #arr[i]=m
            m +=1
        #print(arr)
        #return arr[len(arr)-1]
        return m-1

        
