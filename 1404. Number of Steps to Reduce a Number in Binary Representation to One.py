class Solution:
    def numSteps(self, s: str) -> int:
        ans = 0
        carry = 0
        n = len(s)
        for i in range(n-1, 0, -1):  # Except first digit
            if int(s[i]) + carry == 1:  # Odd number
                carry = 1
                ans += 2  # 2 operations: Add 1 and divide by two
            else:
                ans += 1  # 1 operation: Divide by 2
        return ans + carry


class Solution:
    def numSteps(self, s: str) -> int:
        n=0
        p=0
        for i in range(len(s)-1,-1,-1) :
            n = n + ( 2**p )*int(s[i])
            p +=1
        c=0
        while n != 1:
            if n%2==0 :
                n=n//2
            else :
                n +=1
            c +=1
        return c
