class Solution:

    def reverse(self, x):
        def signCheck(n):
            if n >= 0:
                return 1
            else:
                return -1
    
        sign = signCheck(x)
        x = str(abs(x))
        reverse = x[::-1]
        num = sign * int(reverse)
        
        # check overflow
        if(abs(num) > (2 ** 31 - 1)):
            return 0
        else:
            return num
        
        
