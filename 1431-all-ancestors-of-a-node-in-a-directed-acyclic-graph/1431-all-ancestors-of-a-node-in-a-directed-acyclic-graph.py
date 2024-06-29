class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        d = defaultdict(list)
        for x,y in edges:
            d[y].append(x)

        def find_ancestors(node):
            ancestors = set()
            queue = deque([node])
            while queue:
                current = queue.popleft()
                for parent in d[current]:
                    if parent not in ancestors:
                        ancestors.add(parent)
                        queue.append(parent)
            return sorted(ancestors)

        ans = [find_ancestors(i) for i in range(n)]
        return ans