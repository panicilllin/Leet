from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    max_route=0
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.cal_route(root)
        return self.max_route
    
    def cal_route(self, root: Optional[TreeNode],val:int=None) -> int:
        if root == None:
            return 0
        
        left_route = self.cal_route(root.left,root.val)
        right_route = self.cal_route(root.right,root.val)
        self.max_route = max(left_route+right_route, self.max_route)

        if root.val != val:
            return 0
        else:
            return 1 + max(left_route,right_route)

# AC
