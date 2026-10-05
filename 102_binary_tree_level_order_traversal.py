'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 2026.10.04
class Solution1:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        left_nodes = self.levelOrder(root.left)
        right_nodes = self.levelOrder(root.right)
        res = [[root.val]]
        for i in range(0, max(len(left_nodes), len(right_nodes))):
            curr_level = []
            for nodes in [left_nodes,right_nodes]:
                if i < len(nodes):
                    curr_level.extend(nodes[i])
            res.append(curr_level)
        return res

# 2026.10.04
# BFS
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        queue = deque([root])
        res = []
        while queue:
            curr_level = []
            l_size = len(queue)
            for _ in range(l_size):
                node = queue.popleft()
                if node:
                    curr_level.append(node.val)
                    queue.append(node.left) # type: ignore
                    queue.append(node.right) # type: ignore
            if curr_level:
                res.append(curr_level)
        return res

if __name__ == '__main__':
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(Solution().levelOrder(root))