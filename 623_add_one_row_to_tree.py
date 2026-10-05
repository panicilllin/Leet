from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_node = TreeNode(val=val, left=root)
            return new_node
        self.recusive_tree(root, depth_self=1, depth_to_add=depth, val=val)
        return root

    def recusive_tree(self, root, depth_self, depth_to_add, val):
        if depth_self < depth_to_add - 1:
            if root.left:
                self.recusive_tree(root=root.left, depth_self=depth_self + 1, depth_to_add=depth_to_add, val=val)
            if root.right:
                self.recusive_tree(root=root.right, depth_self=depth_self + 1, depth_to_add=depth_to_add, val=val)
        elif depth_self == depth_to_add - 1:
            new_node_left = TreeNode(val=val, left=root.left)
            root.left = new_node_left
            new_node_right = TreeNode(val=val, right=root.right)
            root.right = new_node_right
        else:
            return

#  AC
