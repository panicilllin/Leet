from typing import Dict, TreeNode


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    node_path={}
    def goodNodes(self, root: TreeNode) -> int:
        self.node_path = {}
        self.cal_node_path(root,None)
        res = 0
        for key, val in self.node_path.items():
            if key.val == max(val):
                res+=1
        return res
        
    
    def cal_node_path(self, root: TreeNode, father_node: TreeNode = None):
        if root is None:
            return
        if father_node == None:
            self.node_path[root]=[root.val]
        else:
            self.node_path[root]=self.node_path[father_node]+[root.val]
        
        self.cal_node_path(root.left,root)
        self.cal_node_path(root.right,root)


            
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.cal_path(root,root.val,0)
        
    def cal_path(self, root: TreeNode, max_val: int=None, res:int=0):
        if root == None:
            return res
        
        if root.val >= max_val:
            max_val = root.val
            res+=1
        res = self.cal_path(root.left, max_val, res)
        res = self.cal_path(root.right, max_val, res)
        return res
 
 # AC