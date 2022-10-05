class Solution:
    def frequencySort(self, s: str) -> str:
        output=""
        count = Counter(s).most_common()
        for c,v in count: 
            output +=c*v 
        return output
