# 847. Problem Title: Shortest Path Visiting All Nodes
# LeetCode Link: https://leetcode.com/problems/

# Problem Title: Shortest Path Visiting All Nodes
# Difficulty: Hard
# Category: Graph, Breadth-First Search (BFS), Bit Manipulation

import collections

class Solution:
    def shortestPathLength(self, graph: list[list[int]]) -> int:
        """
        Calculates the length of the shortest path that visits every node in an undirected graph.

        The problem asks for the minimum path length to visit all nodes in an unweighted graph.
        We can start and end at any node, and revisit nodes/reuse edges. This "shortest path"
        requirement in an unweighted graph immediately suggests a Breadth-First Search (BFS) approach.

        The core challenge is to efficiently track which nodes have been visited. Given the
        small constraint on the number of nodes (`n` <= 12), we can use a bitmask to represent
        the set of visited nodes. A bitmask is an integer where the `k`-th bit is set if node `k`
        has been visited.

        A state in our BFS will be defined by a tuple `(current_node, visited_mask, path_length)`:
        - `current_node`: The node we are currently at.
        - `visited_mask`: A bitmask indicating all unique nodes visited so far on the path to `current_node`.
        - `path_length`: The length of the path taken to reach this state.

        Algorithm:
        1.  **Initialization**:
            *   Get the number of nodes `n` from the `graph`.
            *   If `n` is 1, the path length is 0 (already visited all nodes).
            *   Define `target_mask`: This is a bitmask where all `n` bits are set (e.g., for `n=3`, `target_mask` is `111` in binary, or `7` in decimal). This mask signifies that all nodes have been visited.
            *   Initialize a `collections.deque` named `queue` for the BFS.
            *   Initialize a `set` named `visited_states` to store `(node, mask)` pairs that have already been processed. This prevents re-processing the same state (reaching the same node with the same set of visited nodes via a potentially longer path) and avoids cycles.
            *   Since we can start at any node, add `n` initial states to the queue and `visited_states`: for each node `i` from `0` to `n-1`:
                *   `queue.append((i, 1 << i, 0))` (Node `i` is current, only `i` is visited in mask, path length is 0).
                *   `visited_states.add((i, 1 << i))`

        2.  **BFS Traversal**:
            *   While the `queue` is not empty:
                *   Dequeue a state: `(u, current_mask, dist)`.
                *   **Goal Check**: If `current_mask` is equal to `target_mask`, it means we have successfully visited all nodes. Since BFS explores layer by layer (shortest paths first), `dist` is the shortest path length. Return `dist`.
                *   **Explore Neighbors**: For each neighbor `v` of the current node `u` (from `graph[u]`):
                    *   Calculate `next_mask = current_mask | (1 << v)`. This updates the mask to include node `v` as visited.
                    *   **State Check**: If the new state `(v, next_mask)` has not been visited before (i.e., not in `visited_states`):
                        *   Add `(v, next_mask)` to `visited_states`.
                        *   Enqueue the new state: `queue.append((v, next_mask, dist + 1))`.

        The loop is guaranteed to find a path because the problem implies a path always exists, and `n` is small enough for the state space to be fully explorable.

        """
        n = len(graph)
        
        # Base case: If there's only one node, we've already visited all nodes with 0 path length.
        if n == 1:
            return 0

        # target_mask: A bitmask where all n bits are set.
        # This represents the state where all nodes (from 0 to n-1) have been visited.
        # Example: n=3 -> (1 << 3) - 1 = 8 - 1 = 7 (binary 111)
        target_mask = (1 << n) - 1

        # Queue for BFS: stores tuples of (current_node, visited_mask, path_length)
        queue = collections.deque()
        
        # visited_states: A set to store (node, mask) pairs that have already been processed.
        # This prevents redundant computations and ensures we find the shortest path by
        # not re-exploring paths to an already known state.
        visited_states = set()

        # Initialize BFS: Start from every node as a potential beginning of the shortest path.
        for i in range(n):
            # For each starting node 'i':
            # - current_node is 'i'
            # - visited_mask initially only has the 'i'-th bit set (1 << i)
            # - path_length is 0
            initial_mask = (1 << i)
            queue.append((i, initial_mask, 0))
            visited_states.add((i, initial_mask)) # Mark this initial state as visited

        # Perform BFS
        while queue:
            u, current_mask, dist = queue.popleft()

            # Check if all nodes have been visited (current_mask matches target_mask)
            if current_mask == target_mask:
                # If so, this 'dist' is the shortest path length, as BFS explores layer by layer.
                return dist

            # Explore all neighbors 'v' of the current node 'u'
            for v in graph[u]:
                # Calculate the new mask by including node 'v' in the set of visited nodes
                next_mask = current_mask | (1 << v)

                # If this new state (neighbor 'v', next_mask) has not been visited before:
                if (v, next_mask) not in visited_states:
                    # Mark the state as visited
                    visited_states.add((v, next_mask))
                    # Enqueue the new state with an incremented path length
                    queue.append((v, next_mask, dist + 1))
        
        # This part of the code should ideally not be reached for valid problem constraints,
        # as a path visiting all nodes is generally expected to exist for connected graphs
        # or where N > 0 guarantees a path. If N=0 is possible, it would be an edge case
        # (but N >= 1 per problem statement).
        return -1 # Should indicate an error or an unreachable state if no path exists.

# Time Complexity: O(N * 2^N * N)
#   - N: Number of nodes in the graph.
#   - 2^N: Number of possible bitmasks representing subsets of visited nodes.
#   - N * 2^N: Total number of unique states (node, mask) that can be visited.
#   - For each state, we iterate through its neighbors. In the worst case, a node can have N-1 neighbors.
#     Thus, each state transition takes O(N) time.
#   - The overall time complexity is roughly `Number of States * Max_Degree`, which is `N * 2^N * (N-1)`.
#     This simplifies to O(N^2 * 2^N). Given N <= 12, this is approximately 12^2 * 2^12 = 144 * 4096 = 589,824 operations, which is efficient enough.

# Space Complexity: O(N * 2^N)
#   - The `visited_states` set stores up to `N * 2^N` unique (node, mask) tuples.
#   - The `queue` in the worst case can also hold up to `N * 2^N` states (tuples of `(node, mask, dist)`).
#   - Each tuple stores small integers.
#   - For N=12, this is roughly 12 * 2^12 = 49,152 states, which is a manageable amount of memory.

# Solved: 2026-02-15
