def mat_mul(mat1, mat2, mod):
    res = [[0] * len(mat2[0]) for _ in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                res[i][j] += mat1[i][k] * mat2[k][j]
            res[i][j] %= mod
    return res


def mat_pow(mat, n, mod):
    size = len(mat)
    res = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
    while n > 0:
        if n & 1:
            res = mat_mul(res, mat, mod)
        mat = mat_mul(mat, mat, mod)
        n >>= 1
    return res


class Solution:
    def lengthAfterTransformations(self, s: str, t: int, A: List[int]) -> int:
        M = [[0] * 26 for i in range(26)]
        for i,k in enumerate(A):
            for j in range(i + 1, i + k + 1):
                M[i][j % 26] = 1
        mod = 10 ** 9 + 7
        Mt = mat_pow(M, t, mod)
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        res = mat_mul([count], Mt, mod)
        return sum(res[0]) % mod