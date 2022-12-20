class Solution:
    def minimizeResult(self, exp: str) -> str:
        num1, num2 = exp.split('+')
        minTillNow = inf
        expression = ''
        for i in range(len(num1)):
            a = int(num1[:i] or 1)
            b = int(num1[i:])
            for j in range(1, len(num2) + 1):
                c = int(num2[:j])
                d = int(num2[j:] or 1)
                current = a*(b+c)*d
                if current < minTillNow:
                    minTillNow = current
                    expression = "{}({}+{}){}".format(a,b,c,d)
                    if i == 0: #Removing a = 1 if i = 0
                        expression = expression[1:]
                    if j == len(num2): #Removing d = 1 if j = len(num2)
                        expression = expression[:-1]
                    
                          
        return expression
