class Solution:
    def getLucky(self, s: str, k: int) -> int:
        st=""
        for x in s :
            st += str(ord(x)-96)
        while k :
            t=0
            for x in st :
                t += int(x)
            st=str(t)
            k -=1
        return t