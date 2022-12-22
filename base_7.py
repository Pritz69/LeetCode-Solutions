class Solution:
    def convertToBase7(self, num: int) -> str:
        s = ""
        n = abs(num)
        while n != 0:
            s = str(n % 7) + s
            n = int(n // 7)
        if num > 0:
            return s
        elif num == 0:
            return "0"
        else:
            return "-" + s
