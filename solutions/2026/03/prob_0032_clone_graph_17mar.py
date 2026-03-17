class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        visited = set()
        new_node = {node: node}
        
        def dfs(node):
            if node in visited:
                return new_node[node]
            visited.add(node)
            
            neighbor_map = {}
            for neighbor in node.neighbors:
                neighbor_map[neighbor] = dfs(neighbor)
            
            new_node[node] = Node(node.val, neighbor_map)
            return new_node[node]
        
        return dfs(node)