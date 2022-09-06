from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    level_count={}
    
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        self.level_count = {}
        self.cal_level(root,0)
        res=[]
        for key,value in self.level_count.items():
            res.append(sum(value)/len(value))
        return res
    
    def cal_level(self, root, level):
        if root == None:
            return
        if self.level_count.get(level):
            self.level_count[level].append(root.val)
        else:
            self.level_count[level] = [root.val]
        self.cal_level(root.left, level+1)
        self.cal_level(root.right, level+1)
        