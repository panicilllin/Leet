from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if nums == []:
            return None
        max_idx, max_num = self.find_max(nums)

        root_left = self.constructMaximumBinaryTree(nums=nums[:max_idx])
        root_right = self.constructMaximumBinaryTree(nums=nums[max_idx + 1:])
        root = TreeNode(max_num, root_left, root_right)
        return root

    def find_max(self, nums):
        max_num = 0
        max_idx = None
        for i, num in enumerate(nums):
            if num > max_num:
                max_num = num
                max_idx = i
        return max_idx, max_num
