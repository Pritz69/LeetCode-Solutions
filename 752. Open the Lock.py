class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        visited = set()
        queue = [('0000', 0)]

        while queue:
            current, moves = queue.pop(0)
            if current == target:
                return moves
            if current in deadends or current in visited:
                continue
            visited.add(current)

            for i in range(4):
                for move in [-1, 1]:
                    new_digit = (int(current[i]) + move) % 10
                    new_state = current[:i] + str(new_digit) + current[i+1:]
                    if new_state not in visited:
                        queue.append((new_state, moves + 1))

        return -1
