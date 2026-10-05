from typing import List, Optional

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums)==0:
            return None
        middle = len(nums)//2
        left_node=self.sortedArrayToBST(nums[:middle])
        right_node=self.sortedArrayToBST(nums[middle+1:])
        root = TreeNode(val=nums[middle],left=left_node,right=right_node)
        return root


if __name__ == "__main__":
    a = Solution()
    b = a.sortedArrayToBST(nums = [-10,-3,0,5,9])
    print(b)