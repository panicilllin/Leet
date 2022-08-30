from typing import Optional
from urllib.parse import _NetlocResultMixinStr

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    level_map={}
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.level_map={}
        self.write_node_poi(root,0,0)
        res=0
        # print(self.level_map)
        for val in self.level_map.values():
            res = max(res,val[1]-val[0]+1)
        return res
        
    def write_node_poi(self,root,level,poi):    
        if root is None:
            return
        if self.level_map.get(level):
            self.level_map[level][1] = poi
        else:
            self.level_map[level] = [poi,poi]
        self.write_node_poi(root.left,level+1,poi*2)
        self.write_node_poi(root.right,level+1,poi*2+1)
        # print(self.level_map)

#AC