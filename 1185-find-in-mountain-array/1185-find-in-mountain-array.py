# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n=mountain_arr.length()
        def findpeak():  # Finding one/multiple peak using the concept provided by Striver
            if n==1 :
                return 0
            if mountain_arr.get(0) > mountain_arr.get(1) :
                return 0
            if mountain_arr.get(n-1) > mountain_arr.get(n-2) :
                return n-1
            l=1
            r=n-2
            while l<=r :
                m=(l+r)//2
                curr=mountain_arr.get(m)
                next=mountain_arr.get(m+1)
                prev=mountain_arr.get(m-1)
                if curr > prev and curr > next :
                    return m
                elif curr > prev :
                    l=m+1
                else :
                    r=m-1
            return -1
        p=findpeak()
        search=-1
        l=0
        r=p
        while l<=r :    # After finding the peak, searching in ascending half ( 0 to peak)
            m=(l+r)//2
            curr=mountain_arr.get(m)
            if curr==target :
                search=m
                r=m-1
            if curr > target :
                r=m-1
            else :
                l=m+1
        if search != -1 :
            return search
        l=p+1
        r=n-1
        while l<=r : # If not found in ascending half, searching in descending half...so conidtions of search reversed. (peak to end)
            m=(l+r)//2
            curr=mountain_arr.get(m)
            if curr==target :
                search=m
                break   # Break , as soon as we get the searched element ,, since we want leftmost/minimum index.
            if curr > target :
                l=m+1
            else :
                r=m-1
        #print(p)
        return search
