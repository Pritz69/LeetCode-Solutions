class Solution:
    def countSetBits(self, number):
        count = 0
        while number != 0:
            count += (number & 1)
            number = number >> 1
        return count

    def addSetBits(self, number, bitsToAdd):
        bitPosition = 0
        while bitsToAdd > 0:
            while (number >> bitPosition) & 1 == 1:
                bitPosition += 1
            number = number | (1 << bitPosition)
            bitsToAdd -= 1
        return number

    def removeSetBits(self, number, bitsToRemove):
        while bitsToRemove > 0:
            number = number & (number - 1)
            bitsToRemove -= 1
        return number

    def minimizeXor(self, num1, num2):
        setBitsNum1 = self.countSetBits(num1)
        setBitsNum2 = self.countSetBits(num2)

        if setBitsNum1 == setBitsNum2:
            return num1
        if setBitsNum1 < setBitsNum2:
            return self.addSetBits(num1, setBitsNum2 - setBitsNum1)
        return self.removeSetBits(num1, setBitsNum1 - setBitsNum2)