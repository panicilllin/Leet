# Definition for a binary tree node.
from typing import Optional, List


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

    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        self.makeNode(root=root, level=0)
        levels = [k for k in self.tree.keys()]
        levels.sort()
        res = []
        for i in levels:
            res.append(max(self.tree[i]))
        return res


if __name__ == "__main__":
    a = Solution()
    nodes3_2 = TreeNode(3)
    nodes5 = TreeNode(5)
    nodes9 = TreeNode(9)
    nodes2 = TreeNode(2, nodes9)
    nodes3 = TreeNode(3, nodes5, nodes3_2)
    nodes1 = TreeNode(1, nodes3, nodes2)
    b = a.largestValues(root=nodes1)
    print(b)
