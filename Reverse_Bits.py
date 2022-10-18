class Solution:
	def reverseBits(self, n: int) -> int:

		binary = bin(n)[2:]

		rev = binary[::-1]
		reverse = rev.ljust(32, '0')
		return int(reverse, 2)
