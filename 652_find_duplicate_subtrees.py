# from turtle import right
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    hash_map={}
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.hash_map = {}
        _ = self.dfs(root)
        
        node_map = {}
        for key, val in self.hash_map.items():
            if node_map.get(val):
                node_map[val].append(key)
            else:
                node_map[val] = [key]
        res = []
        print(node_map)
        for fingerprint, nodes in node_map.items():
            if len(nodes) > 1:
                res.append(nodes[0])
        return res
        
    
    def dfs(self, root):
        if root == None:
            return 'None'
        left_map = self.dfs(root.left)
        right_map = self.dfs(root.right)
        root_map = str(root.val) + '-' + left_map + '-' + right_map
        self.hash_map[root] = root_map
        return root_map
        
        
# AC
    