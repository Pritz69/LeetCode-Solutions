class Solution():
    def maxWeightCell(self, N, Edge):
        #your code goes here
        arr=[0]*N
        for i,v in enumerate(Edge) :
            if v >= 0 :
                arr[v] += i
        return arr.index(max(arr))
