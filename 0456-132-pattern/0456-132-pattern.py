class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) <=2 :
            return False
        st=[]
        currmin=float('inf')
        for x in nums :
            while st and x >= st[-1][0] :
                st.pop()
            if st and x < st[-1][0] and x > st[-1][1] :
                return True
            currmin=min(currmin,x)
            st.append([x,currmin])     
        return False
            