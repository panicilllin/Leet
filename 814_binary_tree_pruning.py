from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root.left is None and root.right is None and root.val == 0:
            return None

        if root.left is not None:
            # print(f"left_val={root.left.val}")
            child = self.pruneTree(root=root.left)
            if child is None:
                root.left = None
        if root.right is not None:
            # print(f"right_val={root.right.val}")
            child = self.pruneTree(root=root.right)
            if child is None:
                root.right = None
        if root.left is None and root.right is None and root.val == 0:
            return None
        return root


# AC
