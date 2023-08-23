class Solution {
    public String reorganizeString(String s) {
        Map<Character, Integer> countMap = new HashMap<>();
        for (char c : s.toCharArray()) {
            countMap.put(c, countMap.getOrDefault(c, 0) + 1);
        }
        StringBuilder ans = new StringBuilder();
        PriorityQueue<int[]> maxHeap = new PriorityQueue<>((a, b) -> b[0] - a[0]);
        for (char x : countMap.keySet()) {
            maxHeap.offer(new int[]{ countMap.get(x), (int)x });
        }
        int[] prev = null;
        while (!maxHeap.isEmpty() || prev != null) 
        {
            if (prev != null && maxHeap.isEmpty()) 
            {
                return "";
            }
            int[] current = maxHeap.poll();
            ans.append((char) current[1]);
            current[0]--;
            if (prev != null) 
            {
                maxHeap.offer(prev);
                prev = null;
            }
            if (current[0] != 0) 
            {
                prev = current;
            }
        } 
        return ans.toString();
    }
}
class Solution:
    def reorganizeString(self, s: str) -> str:
        c=Counter(s)
        ans=""
        prev=None
        maxheap=[[-cnt,char]for char,cnt in c.items()]
        heapq.heapify(maxheap)
        while maxheap or prev :
            if prev and not maxheap :
                return ""
            cnt,char=heapq.heappop(maxheap)
            ans += char
            cnt +=1
            if prev :
                heapq.heappush(maxheap,prev)
                prev=None
            if cnt !=0 :
                prev=[cnt,char]
        return ans
