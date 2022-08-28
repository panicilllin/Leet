# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.node_list = []

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        self.node_to_list(root)
        print([i.val for i in self.node_list])
        for i in range(0, len(self.node_list)):
            node = self.node_list[i]
            node.left = None
            if i == len(self.node_list) - 1:
                node.right = None
            else:
                node.right = self.node_list[i + 1]

    def node_to_list(self, root: Optional[TreeNode]) -> None:
        self.node_list.append(root)
        if root.left is not None:
            self.node_to_list(root.left)
        if root.right is not None:
            self.node_to_list(root.right)


if __name__ == "__main__":
    n6 = TreeNode(6)
    n4 = TreeNode(4)
    n3 = TreeNode(3)
    n5 = TreeNode(5, n6)
    n2 = TreeNode(2, n3, n4)
    n0 = TreeNode(1, n2, n5)
    a = Solution()
    b = a.flatten(n0)


# AC