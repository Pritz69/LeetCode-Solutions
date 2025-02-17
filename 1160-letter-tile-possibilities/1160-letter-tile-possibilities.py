class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        seen = set()

        # Sort characters to handle duplicates efficiently
        sorted_tiles = "".join(sorted(tiles))

        # Find all unique sequences and their permutations
        return self._generate_sequences(sorted_tiles, "", 0, seen) - 1

    def _factorial(self, n: int) -> int:
        if n <= 1:
            return 1

        result = 1
        for num in range(2, n + 1):
            result *= num
        return result

    def _count_permutations(self, seq: str) -> int:
        # Calculate permutations using factorial formula
        total = self._factorial(len(seq))

        # Divide by factorial of each character's frequency
        for count in Counter(seq).values():
            total //= self._factorial(count)

        return total

    def _generate_sequences(
        self, tiles: str, current: str, pos: int, seen: set
    ) -> int:
        if pos >= len(tiles):
            # If new sequence found, count its unique permutations
            if current not in seen:
                seen.add(current)
                return self._count_permutations(current)
            return 0

        # Try including and excluding current character
        return self._generate_sequences(
            tiles, current, pos + 1, seen
        ) + self._generate_sequences(tiles, current + tiles[pos], pos + 1, seen)