class Solution:
    def fractionAddition(self, exp):
        i, j, a, b, n = 0, 0, 0, 1, len(exp)
        while j < len(exp):
            i,j = j,exp.find('/', j)
            a2 = int(exp[i:j])
            i, j = j + 1, min(exp.find('+', j) % (n + 1), exp.find('-', j) % (n + 1))
            b2 = int(exp[i:j])
            a, b = a * b2 + b * a2, b * b2
            a, b = a // math.gcd(a, b), b // math.gcd(a, b)
        return str(a) + '/' + str(b)