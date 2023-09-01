O(N)
class Solution:
    def countBits(self, n: int) -> List[int]:
        # [0,1,1,2,1,2,2,3,1,2,2,
        #  0,1,2,3,4,5,6,7,8,9,10,11
        res = [0] * (n + 1)
        power = 1
        for i in range(1, n + 1):
            if i == power * 2:
                power = i
            res[i] = res[i - power] + 1
        return res
O(log n)
class Solution:
    def countBits(self, n: int) -> List[int]:
        l=[]
        for i in range(n+1):
            s=bin(i)[2:]
            l.append(s.count('1'))
        return l
