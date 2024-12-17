class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = Counter(s)
        sorted_chars = sorted(freq.keys(), reverse=True)  
        ans = []
        while sorted_chars:
            curr = sorted_chars[0]
            if freq[curr] > 0:
                count = min(freq[curr], repeatLimit)
                ans.append(curr * count)
                freq[curr] -= count

                if freq[curr] == 0:
                    sorted_chars.pop(0)

                if freq[curr] > 0:
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
                sorted_chars.pop(0)

        return ''.join(ans)
            

