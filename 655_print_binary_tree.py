from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    height=0
    ans_matrix = []

    def cal_height(self, root, level):
        if root is None:
            return
        self.height = max(self.height, level)
        self.cal_height(root.left, level + 1)
        self.cal_height(root.right, level + 1)

    def dfs(self,root,level,n):
        if root is None:
            return
        self.ans_matrix[level][n] = str(root.val)
        self.dfs(root.left,level+1,n-int(math.pow(2,self.height-level-1)))
        self.dfs(root.right,level+1,n+int(math.pow(2,self.height-level-1)))

    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        self.cal_height(root,0)
        m = self.height + 1
        n = int(math.pow(2,m))-1
        self.ans_matrix = [["" for j in range(n)] for i in range(m)]
        print(self.ans_matrix)
        self.dfs(root,0,int((n-1)/2))
        return self.ans_matrix

# AC

