from typing import List, Optional

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Approach: 
        Time Complexity: O(N)
        Space Complexity: O(W), where W is the number of levels in the tree
        """
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.levelOrder(None))  # Expected: []
    print(s.levelOrder(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))  # Expected: [[3],[9,20],[15,7]]