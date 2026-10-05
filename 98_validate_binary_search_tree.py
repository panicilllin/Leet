from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        root_bst,_,_,=self.recusive_BST(root)
        return root_bst

    def recusive_BST(self, root: Optional[TreeNode]) -> bool:
        if root.left is not None:
            if root.left.val >= root.val:
                return False,None,None
            left_bst,left_min,left_max =  self.recusive_BST(root.left)
            if left_bst is False or left_max >= root.val:
                return False,None,None
        else:
            left_min=root.val

        if root.right is not None:
            if root.right.val <= root.val:
                return False,None,None
            right_bst, right_min, right_max = self.recusive_BST(root.right)
            if right_bst is False or right_min <= root.val:
                return False, None, None
        else:
            right_max = root.val
        min_val = left_min
        max_val = right_max
        return True,min_val,max_val


class Solution1:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(root, min, max):
            if root.val <= min or root.val >= max:
                return False
            if root.left and not valid(root.left, min, root.val):
                return False
            if root.right and not valid(root.right, root.val, max):
                return False
            return True

        return valid(root, float('-inf'), float('inf'))
# AC