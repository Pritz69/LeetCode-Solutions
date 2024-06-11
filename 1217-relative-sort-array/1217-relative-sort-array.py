class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d={}
        for x in arr1:
            d[x]=d.get(x,0)+1
        i =0
        for x in arr2 :
            for _ in range(d[x]) :
                arr1[i]=x
                i +=1
            d.pop(x)
        d=sorted(d.items(),key=lambda x:x[0])
        for x in d :
            for _ in range(x[1]) :
                arr1[i]=x[0]
                i +=1
        return arr1


        