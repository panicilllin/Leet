from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return None
        
        if root.val < val:
            new_node = TreeNode(val=val, left=root)
            return new_node
                
        new_right = self.insertIntoMaxTree(root.right,val)
        if new_right != None:
            root.right = new_right
            return root

        new_left = self.insertIntoMaxTree(root.left,val)
        if new_left != None:
            root.left = new_left
            return root
        
        return root


class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = TreeNode(val)
        prev = None
        cur = root
        while (cur != None and cur.val > val):
            prev = cur
            cur = cur.right
        if prev == None:
            node.left = cur
            return node
        else:
            prev.right = node
            node.left = cur
            return root