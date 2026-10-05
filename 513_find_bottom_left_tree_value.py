# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.tree = {}

    def makeNode(self, root: Optional[TreeNode], level) -> int:
        node_level = level
        if self.tree.get(node_level):
            self.tree[node_level].append(root.val)
        else:
            self.tree[node_level] = [root.val]
        if root.left:
            self.makeNode(root=root.left, level=node_level + 1)
        if root.right:
            self.makeNode(root=root.right, level=node_level + 1)

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.makeNode(root=root, level=0)
        levels = [k for k in self.tree.keys()]
        levels.sort()
        return self.tree[levels[-1]][0]


if __name__ == "__main__":
    a = Solution()
    nodes = {}
    nodes[7] = TreeNode(7)
    nodes[4] = TreeNode(4)
    nodes[5] = TreeNode(4, nodes[7])
    nodes[6] = TreeNode(6)
    nodes[2] = TreeNode(2, nodes[4])
    nodes[3] = TreeNode(3, nodes[5], nodes[7])
    nodes[1] = TreeNode(2, nodes[2], nodes[3])
    b = a.findBottomLeftValue(root=nodes[1])
    print(b)
