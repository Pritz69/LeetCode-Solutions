class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = Counter(s)
        sorted_chars = sorted(freq.keys(), reverse=True)  # Descending order of characters
        ans = []

        while sorted_chars:
            # Pick the highest available character
            curr = sorted_chars[0]
            if freq[curr] > 0:
                # Add up to repeatLimit of the current character
                count = min(freq[curr], repeatLimit)
                ans.append(curr * count)
                freq[curr] -= count

                if freq[curr] == 0:
                    # Remove the character from sorted_chars if exhausted
                    sorted_chars.pop(0)

                if freq[curr] > 0:
                    # If the character still exists, add the next available character
                    if len(sorted_chars) > 1:
                        next_char = sorted_chars[1]
                        ans.append(next_char)
                        freq[next_char] -= 1

                        if freq[next_char] == 0:
                            sorted_chars.pop(1)
                    else:
                        # If no next character, stop to avoid consecutive repeats
                        break
            else:
                # Remove exhausted character
                sorted_chars.pop(0)

        return ''.join(ans)
            

