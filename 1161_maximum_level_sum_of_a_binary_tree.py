from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level_count = {}
        self.count_level(root=root, level=1, level_count=level_count)
        res = None
        max_count = None
        print(level_count)
        for level in level_count.keys():
            if not res:
                max_count = level_count[level]
                res = level

            if level_count[level] > max_count:
                res = level
                max_count = level_count[level]
            elif level_count[level] == max_count:
                res = min(res, level)
            # print(res,max_count)
        return res

    def count_level(self, root, level, level_count):

        if not level_count.get(level):
            level_count[level] = root.val
        else:
            level_count[level] += root.val
        # print(level,root.val,self.level_count[level])
        if root.left:
            self.count_level(root=root.left, level=level + 1, level_count=level_count)
        if root.right:
            self.count_level(root=root.right, level=level + 1, level_count=level_count)

# AC
