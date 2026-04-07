def validateBST(root, min_val=float('-inf'), max_val=float('inf')):
    if not root:
        return True

    val = root.val
    if val <= min_val or val >= max_val:
        return False

    return (validateBST(root.left, min_val, val) and
            validateBST(root.right, val, max_val))


# --- Test Cases ---
if __name__ == '__main__':
    # Create a binary search tree for testing
    #       2
    #      / \
    #     1   3
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    s = Solution()
    print(validateBST(root))  # Expected: True

    # Create another binary search tree for testing
    #       5
    #      / \
    #     4   6
    #    /
    #   3
    root2 = TreeNode(5)
    root2.left = TreeNode(4)
    root2.right = TreeNode(6)
    root2.left.left = TreeNode(3)

    print(validateBST(root2))  # Expected: False