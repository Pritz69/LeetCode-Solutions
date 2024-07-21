class Solution:
    def buildMatrix(
        self,
        k: int,
        rowConditions: List[List[int]],
        colConditions: List[List[int]],
    ) -> List[List[int]]:
        # Store the topologically sorted sequences.
        order_rows = self.__topoSort(rowConditions, k)
        order_columns = self.__topoSort(colConditions, k)

        # If no topological sort exists, return empty array.
        if not order_rows or not order_columns:
            return []
        matrix = [[0] * k for _ in range(k)]
        pos_row = {num: i for i, num in enumerate(order_rows)}
        pos_col = {num: i for i, num in enumerate(order_columns)}

        for num in range(1, k + 1):
            if num in pos_row and num in pos_col:
                matrix[pos_row[num]][pos_col[num]] = num
        return matrix

    def __topoSort(self, edges: List[List[int]], n: int) -> List[int]:
        adj = defaultdict(list)
        order = []
        visited = [0] * (n + 1)
        has_cycle = [False]

        # Build adjacency list
        for x, y in edges:
            adj[x].append(y)
        # Perform DFS for each node
        for i in range(1, n + 1):
            if visited[i] == 0:
                self.__dfs(i, adj, visited, order, has_cycle)
                # Return empty if cycle detected
                if has_cycle[0]:
                    return []
        # Reverse to get the correct order
        order.reverse()
        return order

    def __dfs(
        self,
        node: int,
        adj: defaultdict,
        visited: List[int],
        order: List[int],
        has_cycle: List[bool],
    ):
        # Mark node as visiting
        visited[node] = 1
        for neighbor in adj[node]:
            if visited[neighbor] == 0:
                self.__dfs(neighbor, adj, visited, order, has_cycle)
                # Early exit if a cycle is detected
                if has_cycle[0]:
                    return
            elif visited[neighbor] == 1:
                # Cycle detected
                has_cycle[0] = True
                return
        # Mark node as visited
        visited[node] = 2
        # Add node to the order
        order.append(node)