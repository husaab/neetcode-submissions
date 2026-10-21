class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        edge_map = {}
        visited = set()
        result = 0

        for edge, child in edges:
            edge_map.setdefault(edge, []).append(child)
            edge_map.setdefault(child, []).append(edge)

        def dfs(edge):
            if edge in visited:
                return
            
            neighbors = edge_map.get(edge, [])

            visited.add(edge)
            for neighbor in neighbors:
                dfs(neighbor)
            
            return 1


        for num in range(n):
            if num in visited:
                continue
            result+=dfs(num)

        return result