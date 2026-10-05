from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    max_level=0
    max_sum=0

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.find_max_level(root,level=0)
        self.sum_max_level(self,root,level=0)
        return self.max_sum

    def sum_max_level(self,root,level):
        if root is None:
            return
        if level == self.max_level:
            self.max_sum+=root.value
            return
        self.sum_max_level(root.left, level + 1)
        self.sum_max_level(root.right, level + 1)
        return

    def find_max_level(self,root,level):
        if root is None:
            return
        if level>self.max_level:
            self.max_level = level

        self.find_max_level(root.left,level+1)
        self.find_max_level(root.right,level+1)
        return
#AC

class Solution_test:
    max_level=0
    sum_map=[]

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.re_tree(root,0)

    def re_tree(self,root,level):
        if root is None:
            return
        print(root.val)
        if root.left:
            self.re_tree(root.left,level+1)
        if root.right:
            self.re_tree(root.right, level + 1)
