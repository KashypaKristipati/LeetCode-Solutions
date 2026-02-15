from typing import List, Optional
from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        """
        Approach: 
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        We use a dictionary to store the cloned nodes and their corresponding original nodes.
        Then we perform DFS on the graph and for each visited node, we create a new node in the clone graph
        and update its neighbors with the cloned versions of the original nodes' neighbors.

        :param node: The root node of the graph
        :return: The root node of the cloned graph
        """
        
        # Create a dictionary to store the cloned nodes and their corresponding original nodes
        visited = {}
        
        # Define a helper function for DFS
        def dfs(node):
            if node in visited:
                return visited[node]
            
            # If the node is not visited, create a new node in the clone graph
            cloned_node = Node(node.val)
            visited[node] = cloned_node
            
            # Perform DFS on the neighbors of the current node
            for neighbor in node.neighbors:
                cloned_neighbor = dfs(neighbor)
                cloned_node.neighbors.append(cloned_neighbor)
            
            return cloned_node
        
        # Start DFS from the root node
        return dfs(node)