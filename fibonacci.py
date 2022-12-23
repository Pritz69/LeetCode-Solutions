class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1: return n
        first = 0
        second = 1
        for i in range(1,n):
            third = first + second
            first = second
            second = third
        return second
